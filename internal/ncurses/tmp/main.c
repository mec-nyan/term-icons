#include "niceties.h"
#include <curses.h>
#include <locale.h>

int main() {

	char * loc = setlocale(LC_ALL, "en_US.UTF-8");
	if (loc == NULL) {
		return 42;
	}

	initscr();
	cbreak();
	noecho();

	WINDOW* win = newwin(4, 20, 4, 4);

	mvwaddstr(win, 1, 1, loc);

	wgetch(win);

	int border = 0;
	int c	   = 0;
	while ((c = wgetch(win)) != 'q') {
		switch (border) {
		case 0:
			sharp_box(win);
			break;
		case 1:
			rounded_box(win);
			break;
		case 2:
			dotted_box(win);
			break;
		case 3:
			dotted_rounded_box(win);
			break;
		case 4:
			fat_box(win);
			break;
		case 5:
			fat_dotted_box(win);
			break;
		case 6:
			double_box(win);
			break;
		}
		border++;
		if (border == 7) {
			border = 0;
		}
	}

	echo();
	nocbreak();
	endwin();

	return 0;
}
