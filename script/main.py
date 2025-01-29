#!/usr/bin/env python3
"""Search icons by word/name."""

import curses
import locale
import sys

from icons import icons
import ui
import search
import clip

# Find the longest string in the keys of icons.
MAX_KEY_LEN = 0
for k in icons.keys():
    if len(k) > MAX_KEY_LEN:
        MAX_KEY_LEN = len(k)

# Search function to use. Exact match by default.
search_func = search.simple_search
for arg in sys.argv:
    if arg == "-fuzzy":
        search_func = search.fuzzy_search


welcome_msg = """\
Welcome, traveller!

This tool will help you find your favourite
icons by name or description.
Enjoy!


Just type something to begin searching.


<C-n> Next element on the result list.

<C-p> Previous element on the result lits.

<Enter> Copy selection to clipboard.

Use `:` to enter commands.

Use `/` to go back to search mode.
""".split("\n")

command_msg = """\
Your search is saved.
Press / to go back.

Or type a command and hit <Enter>

Available commands

:help
:exact
:fuzzy
:show list
:show grid
:go back
:quit
""".split("\n")


class Tipper:
    index = 0
    tips = [
        # Tips to show when there's no results.
        # TODO: Add more and better tips.
        "Are you sure that's how you spell it?",
        "Sorry, couldn't find that thing...",
        "Try again!",
        "Maybe you could try a fuzzy search",
    ]

    def next_tip(self):
        self.index += 1
        if self.index == len(self.tips):
            self.index = 0
        return self.tips[self.index]


def main(screen):
    """Do stuff!"""

    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    MIN_DIM = (25, MAX_KEY_LEN + 4)
    screen = curses.newwin(0, 0, 0, 0)
    height, width = screen.getmaxyx()

    if height < MIN_DIM[0] or width < MIN_DIM[1]:
        raise "Screen is too small to do stuff!"

    curses.start_color()

    palette = {
            "background": (55, 62, 72),
            "search": (95, 211, 188),
            "command": (255, 230, 128),
            "results": (170, 135, 222),
            "tips": (135, 170, 222),
            }

    def to_curses_colour(c):
        return int((1000 / 255) * c)

    def to_curses_rgb(r, g, b):
        rr = to_curses_colour(r)
        gg = to_curses_colour(g)
        bb = to_curses_colour(b)
        return (rr, gg, bb)

    if curses.can_change_color():
        curses.init_color(231, *to_curses_rgb(*palette["background"]))
        curses.init_color(232, *to_curses_rgb(*palette["search"]))
        curses.init_color(233, *to_curses_rgb(*palette["command"]))
        curses.init_color(234, *to_curses_rgb(*palette["results"]))
        curses.init_color(235, *to_curses_rgb(*palette["tips"]))
        curses.init_pair(1, 232, 231)
        search_fg = curses.color_pair(1)

        curses.init_pair(2, 233, 231)
        command_fg = curses.color_pair(2)

        curses.init_pair(3, 235, 231)
        tips_fg = curses.color_pair(3)

        curses.init_pair(4, 234, 231)
        results_fg = curses.color_pair(4)

    else:
        curses.init_pair(1, 48, 0)
        search_fg = curses.color_pair(1)

        curses.init_pair(2, 35, 0)
        tips_fg = curses.color_pair(2)

        curses.init_pair(3, 104, 0)
        results_fg = curses.color_pair(3)

        curses.init_pair(4, 221, 0)
        command_fg = curses.color_pair(4)

    screen.bkgdset(search_fg)
    screen.clear()
    screen.refresh()

    # curses.init_pair(5, 105, -1)
    # tip_fg = curses.color_pair(5)
    #
    # curses.init_pair(6, 172, -1)
    # cmd_tip_fg = curses.color_pair(6)

    # Title
    title_h = 5
    title_w = curses.newwin(title_h, width, 0, 0)
    little_help = "Type to search    <ESC> quits    ':help<Enter>' for help"
    title = {"search": "Search  ", "command": "Command  "}

    # Search bar
    bar_h, bar_w = 3, 40
    bar_x = (width - bar_w) // 2
    bar_y = 5

    outer = curses.newwin(bar_h, bar_w, bar_y, bar_x)
    outer.refresh()

    # Search result
    results_y = bar_y + bar_h
    results_h = height - (results_y + 2)  # leave space for the status line.
    results = curses.newwin(results_h, width, results_y, 0)
    results.bkgdset(results_fg)

    status_line = curses.newwin(1, width, height - 2, 0)
    status_line.bkgdset(tips_fg)

    icon_w = 2  # Full width icon plus next space to flow into.
    unicode_w = 10  # "U+" + a maximum of 8 hex digits.
    separator_w = 2  # haw many spaces between fields/columns.

    search_content = []
    saved = []
    selected = 0
    tipper = Tipper()
    mode = "search"
    while True:
        title_w.bkgdset(tips_fg)
        title_w.clear()
        title_w.addstr(little_help.center(width))
        if mode == "search":
            title_w.bkgdset(search_fg)
            title_w.addstr(3, ((width - len(title["search"])) // 2), title["search"])
            title_w.noutrefresh()
            outer.bkgdset(search_fg)
        elif mode == "command":
            title_w.bkgdset(command_fg)
            title_w.addstr(3, ((width - len(title["command"])) // 2), title["command"])
            title_w.noutrefresh()
            outer.bkgdset(command_fg)
        pattern = "".join(search_content)

        findings = search_func(icons, pattern, (results_h - 2) // 2)

        status_line.clear()
        if pattern and mode == "search":
            status_line.addstr(
                0,
                2,
                f'Found {len(findings)} item{len(findings)>1 and 's' or ''} matching "{pattern}"'.center(
                    width - 4
                ),
            )

        if mode == "command":
            status_line.addstr(0, 2, "cmd".center(width - 4))
        status_line.noutrefresh()

        results.clear()

        # TODO: Maybe add a separate window for Help.
        if not findings and not pattern:
            for i in range(len(welcome_msg)):
                if i < 5:
                    results.addstr(2 + i, 0, welcome_msg[i].center(width))
                else:
                    results.addstr(2 + i, bar_x, welcome_msg[i])

        if pattern and not findings and mode == "search":
            results.addstr(2, 0, tipper.next_tip().center(width))

        if mode == "command":
            # results.bkgdset(cmd_tip_fg)
            for i in range(len(command_msg)):
                results.addstr(2 + i, bar_x, command_msg[i])

        display_results_w = MAX_KEY_LEN + unicode_w + icon_w + separator_w * 2
        padding = (width - display_results_w) // 2
        name_col = padding
        icon_col = name_col + MAX_KEY_LEN + separator_w

        for i in range(len(findings)):
            selected_attr = 0
            if i < results_h:
                if i == selected:
                    # Highglight selected line.
                    # TODO: Use a better approach (i.e. change the line bg).
                    selected_attr = curses.A_REVERSE | curses.A_BOLD
                row = 1 + i * 2
                results.move(row, name_col)
                pos = 0

                # icon name.
                for letter in findings[i]:
                    if pos < len(pattern) and letter == pattern[pos]:
                        results.addch(letter, search_fg | selected_attr)
                        pos += 1
                    else:
                        results.addch(letter, selected_attr)

                icon = icons[findings[i]]
                unicode = hex(ord(icon))
                unicode = unicode.replace("0x", "U+")
                results.addstr(row, icon_col, f"{icon:2}  ", search_fg)
                results.addstr(f"{unicode:>10}")
                if i == selected:
                    results.addstr("  *", curses.A_BOLD | search_fg)

        results.noutrefresh()
        outer.clear()
        ui.rounded_box(outer)

        outer.addstr(1, 2, pattern)
        c = outer.getch()
        c = chr(c)
        if c.isalnum() or c in " -_":
            selected = 0
            if len(search_content) < bar_w - 4:
                search_content.append(c)
        if c == "\x1b":
            break
        elif c in ["\x7f", ""]:
            selected = 0
            if len(search_content):
                search_content.pop()
            if mode == "command" and not len(search_content):
                mode = "search"
        elif c == "":
            if selected < len(findings) - 1:
                selected += 1
            else:
                selected = 0
        elif c == "":
            if selected > 0:
                selected -= 1
            else:
                selected = len(findings) - 1
        elif c == "":
            if mode == "search":
                search_content.clear()
            elif mode == "command":
                search_content = search_content[:1]
        elif c == "\n":
            if mode == "search":
                clip.to_clipboard(icons[findings[selected]])
            elif mode == "command":
                #TODO: execute command or give help.
                pass
        elif c == ":":
            saved = search_content[:]
            search_content = [":"]
            mode = "command"
        elif c == "/":
            search_content = saved[:]
            saved = []  # Is this really necessary?
            mode = "search"

        curses.doupdate()


if __name__ == "__main__":
    curses.wrapper(main)
