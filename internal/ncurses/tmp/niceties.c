#include "niceties.h"
#include <string.h>
//   WARNING! 
// This requires a version of ncurses higher thatn 6.2!

const char hline_thin[]		  = "─";
const char hline_dotted[]	  = "╌";
const char hline_fat[]		  = "━";
const char hline_dotted_fat[] = "╍";
const char hline_double[]	  = "═";

const char vline_thin[]		  = "│";
const char vline_dotted[]	  = "┆";
const char vline_fat[]		  = "┃";
const char vline_dotted_fat[] = "┇";
const char vline_double[]	  = "║";

const char topleft_sharp[]	 = "┌";
const char topleft_rounded[] = "╭";
const char topleft_fat[]	 = "┏";
const char topleft_double[]	 = "╔";

const char topright_sharp[]	  = "┐";
const char topright_rounded[] = "╮";
const char topright_fat[]	  = "┓";
const char topright_double[]  = "╗";

const char botleft_sharp[]	 = "└";
const char botleft_rounded[] = "╰";
const char botleft_fat[]	 = "┗";
const char botleft_double[]	 = "╚";

const char botright_sharp[]	  = "┘";
const char botright_rounded[] = "╯";
const char botright_fat[]	  = "┛";
const char botright_double[]  = "╝";

int put_border(WINDOW* win, BorderStyle* style) {
	int height = getmaxy(win);
	int width  = getmaxx(win);

	wmove(win, 0, 0);
	if (waddstr(win, style->tl) == ERR)
		return ERR;
	if (waddstr(win, style->tr) == ERR)
		return ERR;
	wmove(win, 0, 1);
	for (int i = 0; i < width - 2; i++) {
		if (winsstr(win, style->hl) == ERR)
			return ERR;
	}

	for (int i = 1; i < height - 1; i++) {
		mvwaddstr(win, i, 0, style->vl);
		mvwaddstr(win, i, width - 1, style->vl);
	}

	wmove(win, height - 1, 0);
	if (waddstr(win, style->bl) == ERR)
		return ERR;
	if (waddstr(win, style->br) == ERR)
		return ERR;
	wmove(win, height - 1, 1);
	for (int i = 0; i < width - 2; i++) {
		if (winsstr(win, style->hl) == ERR)
			return ERR;
	}
	return 0;
}

BorderStyle border_sharp = {
	.vl = vline_thin,
	.hl = hline_thin,
	.tl = topleft_sharp,
	.tr = topright_sharp,
	.bl = botleft_sharp,
	.br = botright_sharp,
};

BorderStyle border_rounded = {
	.vl = vline_thin,
	.hl = hline_thin,
	.tl = topleft_rounded,
	.tr = topright_rounded,
	.bl = botleft_rounded,
	.br = botright_rounded,
};

BorderStyle border_dotted = {
	.vl = vline_dotted,
	.hl = hline_dotted,
	.tl = topleft_sharp,
	.tr = topright_sharp,
	.bl = botleft_sharp,
	.br = botright_sharp,
};

BorderStyle border_dotted_rounded = {
	.vl = vline_thin,
	.hl = hline_thin,
	.tl = topleft_rounded,
	.tr = topright_rounded,
	.bl = botleft_rounded,
	.br = botright_rounded,
};

BorderStyle border_fat = {
	.vl = vline_fat,
	.hl = hline_fat,
	.tl = topleft_fat,
	.tr = topright_fat,
	.bl = botleft_fat,
	.br = botright_fat,
};

BorderStyle border_fat_dotted = {
	.vl = vline_dotted_fat,
	.hl = hline_dotted_fat,
	.tl = topleft_fat,
	.tr = topright_fat,
	.bl = botleft_fat,
	.br = botright_fat,
};

BorderStyle border_double = {
	.vl = vline_double,
	.hl = hline_double,
	.tl = topleft_double,
	.tr = topright_double,
	.bl = botleft_double,
	.br = botright_double,
};

int sharp_box(WINDOW* win) {
	return put_border(win, &border_sharp);
}

int rounded_box(WINDOW* win) {
	return put_border(win, &border_rounded);
}

int dotted_box(WINDOW* win) {
	return put_border(win, &border_dotted);
}

int dotted_rounded_box(WINDOW* win) {
	return put_border(win, &border_dotted_rounded);
}

int fat_box(WINDOW* win) {
	return put_border(win, &border_fat);
}

int fat_dotted_box(WINDOW* win) {
	return put_border(win, &border_fat_dotted);
}

int double_box(WINDOW* win) {
	return put_border(win, &border_double);
}

Rect new_rect(RectSize size, RectPos pos) {
	WINDOW* win = newwin(size.height, size.width, pos.y, pos.x);
	if (win == NULL) {
		return (Rect) {
			.win  = 0,
			.geom = { .ws = { 0, 0 }, .wp = { 0, 0 } },
		};
	}
	return (Rect) {
		.win  = win,
		.geom = { .ws = size, .wp = pos },
	};
}

int rect_write(Rect* rect, const char* text) {
	// TODO: This function is supposed to write properly:
	// Don't break words (add a newline).
	// If the text didn't fit inside the rect, write as much as it fits
	// and return the position of the next word.
	// Otherwise returns the length of the string so you know it all
	// has been written.
	waddstr(rect->win, text);
	return 0;
}

void rect_refresh(Rect* rect) {
	wrefresh(rect->win);
}

void rect_clear(Rect* rect) {
	wclear(rect->win);
}

BorderedRect new_bordered_rect(RectSize size, RectPos pos, Padding pad, BorderStyle style) {
	RectSize inner_size = {
		.width	= size.width - (pad.left + pad.right + 2),
		.height = size.height - (pad.top + pad.bottom + 2),
	};
	RectPos inner_pos = {
		.y = pos.y + 1 + pad.top,
		.x = pos.x + 1 + pad.left,
	};
	return (BorderedRect) {
		.outer = new_rect(size, pos),
		.inner = new_rect(inner_size, inner_pos),
		.style = style,
	};
}

int b_rect_border(BorderedRect* brect) {
	return put_border(brect->outer.win, &brect->style);
}

int b_rect_title(BorderedRect* rect, int pos, int margin, const char* title) {
	// Position: -1 == left, 0 == center, 1 == right.
	// TODO: Use a better function to calculate the length of the text.
	if (pos < -1 || pos > 1) {
		return -1;
	}

	int		width = rect->outer.geom.ws.width;
	WINDOW* win	  = rect->outer.win;

	int len = strlen(title);
	if (len + margin > width) {
		return -1;
	}

	if (pos == 1) {
		margin = width - (len + margin);
	} else if (pos == 0) {
		margin = (width - len) / 2;
	}

	mvwaddstr(win, 0, margin, title);
	return 0;
}

int b_rect_write(BorderedRect* brect, const char* text) {
	return rect_write(&brect->inner, text);
}

void b_rect_refresh(BorderedRect* brect) {
	rect_refresh(&brect->outer);
	rect_refresh(&brect->inner);
}

void b_rect_clear(BorderedRect* brect) {
	rect_clear(&brect->outer);
	rect_clear(&brect->inner);
}
