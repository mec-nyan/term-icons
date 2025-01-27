#!/usr/bin/env python3
"""Search icons by word/name."""

import curses
import locale
import sys

from icons import icons
import ui
import search

MAX_NAME_LEN = 0
for k in icons.keys():
    if len(k) > MAX_NAME_LEN:
        MAX_NAME_LEN = len(k)

search_func = search.simple_search
for arg in sys.argv:
    if arg == "-fuzzy":
        search_func = search.fuzzy_search

def main(_):
    """Do stuff!"""

    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    MIN_DIM = (25, MAX_NAME_LEN + 4)
    screen = curses.newwin(0, 0, 0, 0)
    height, width = screen.getmaxyx()

    if height < MIN_DIM[0] or width < MIN_DIM[1]:
        raise "Screen is too small to do stuff!"

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, 48, -1)
    green_fg = curses.color_pair(1)

    curses.init_pair(2, 75, -1)
    results_fg = curses.color_pair(2)

    # Title
    title_h = 5
    title_w = curses.newwin(title_h, width, 0, 0)
    title_w.addstr("Press <ESC> to quit")
    title_w.bkgdset(green_fg)
    title = "Search  "
    title_w.addstr(3, ((width - len(title)) // 2), title)
    title_w.refresh()

    # Search bar
    bar_h, bar_w = 3, 40
    bar_x = (width - bar_w) // 2
    bar_y = 5

    outer = curses.newwin(bar_h, bar_w, bar_y, bar_x)
    outer.bkgdset(green_fg)
    outer.refresh()

    # Search result
    results_y = bar_y + bar_h
    results_h = height - results_y
    results = curses.newwin(results_h, width, results_y, 0)
    results.bkgdset(results_fg)

    search_content = []
    while True:
        pattern = "".join(search_content)

        findings = search_func(icons, pattern, (results_h - 2) // 2)

        results.clear()

        display_results_w = MAX_NAME_LEN + 4
        padding = (width - display_results_w) // 2
        for i in range(len(findings)):
            if i < results_h:
                results.move(1 + i * 2, padding)
                pos = 0
                for letter in findings[i]:
                    if pos < len(pattern) and letter == pattern[pos]:
                        results.addch(letter, green_fg)
                        pos += 1
                    else:
                        results.addch(letter)
                results.addstr(1 + i * 2, padding + MAX_NAME_LEN, icons[findings[i]])


        results.refresh()
        outer.clear()
        ui.rounded_box(outer)

        outer.addstr(1, 2, pattern)
        c = outer.getch()
        c = chr(c)
        if c.isalnum() or c in " -_":
            if len(search_content) < bar_w - 4:
                search_content.append(c)
        if c == "\x1b":
            break
        elif c in ["\x7f", ""]:
            if len(search_content):
                search_content.pop()


if __name__ == "__main__":
    curses.wrapper(main)
