#include "niceties.h"
#include <curses.h>
#include <locale.h>
#include <stdio.h>

int main() {

	/*printf("Usin curses: %s\n", NCURSES_VERSION);*/
	/*return 0;*/

	char* loc = setlocale(LC_ALL, "en_US.UTF-8");
	if (loc == NULL) {
		return 42;
	}

	initscr();
	cbreak();
	noecho();

	WINDOW* win = newwin(4, 20, 4, 4);

	mvwaddstr(win, 1, 1, loc);

	int border = 0;
	int c	   = 0;
	int err	   = 0;
	while ((c = wgetch(win)) != 'q') {
		wclear(win);
		switch (border) {
		case 0:
			err = sharp_box(win);
			break;
		case 1:
			err = rounded_box(win);
			break;
		case 2:
			err = dotted_box(win);
			break;
		case 3:
			err = dotted_rounded_box(win);
			break;
		case 4:
			err = fat_box(win);
			break;
		case 5:
			err = fat_dotted_box(win);
			break;
		case 6:
			err = double_box(win);
			break;
		}
		border++;
		if (border == 7) {
			border = 0;
		}
		mvwprintw(win, 1, 1, "Error: %d", err);
	}

	RectSize	 size = { .height = 10, .width = 30 };
	RectPos		 pos  = { .y = 6, .x = 10 };
	Padding		 pad  = {.top = 1, .right = 2, .bottom = 1, .left = 2};
	BorderedRect br	  = new_bordered_rect(size, pos, pad, border_dotted);
	b_rect_border(&br);
	b_rect_title(&br, -1, 4, " ima box ");
	b_rect_write(&br, "This is some text. Here you go.");
	b_rect_refresh(&br);
	wgetch(br.inner.win);

	echo();
	nocbreak();
	endwin();

	return 0;
}
