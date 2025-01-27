"""Some UI improvements."""

rounded_topleft = "╭"
rounded_botleft = "╰"
rounded_topright = "╮"
rounded_botright = "╯"
vline_slim = "│"
hline_slim = "─"


def rounded_box(win):
    # TODO: Find out why it fails to print "vline_slim"...
    # For now, we use box() instead.
    win.box()
    height, width = win.getmaxyx()
    win.addstr(0, 0, rounded_topleft)
    win.addstr(height - 1, 0, rounded_botleft)
    win.addstr(0, width - 1, rounded_topright)
    win.insstr(height - 1, width - 1, rounded_botright)
