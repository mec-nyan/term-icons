#!/usr/bin/env python3
"""
Test printing Unicode chars above 0xFFFF.

For some reason, those characters/codepoints "consume" a space on the line...
"""

from icons import icons

import curses


def main(_):
    curses.start_color()
    curses.init_pair(1, 5, 240)
    bkg = curses.color_pair(1)

    _icons = [
        icons["nf-linux-xfce"] + " ",
        icons["nf-linux-ubuntu"] + " ",
        icons["nf-md-abjad_hebrew"] + " ",
        icons["nf-linux-xorg"] + " ",
    ]

    win = curses.newwin(0, 0, 0, 0)
    win.bkgd(bkg)

    # For some reason, doing a "getch" avoids "bkgd" to scramble the text!
    curses.halfdelay(5)
    win.getch()
    curses.nocbreak()
    curses.cbreak()

    rows, cols = win.getmaxyx()

    y_pos = 4
    x_pos = 8

    for i in _icons:
        s = f"\tThis is some text with {i}\tHello {i}"
        win.move(y_pos, x_pos)
        for c in s:
            win.addch(c)
        y_pos += 1

    win.getch()


if __name__ == "__main__":
    curses.wrapper(main)
