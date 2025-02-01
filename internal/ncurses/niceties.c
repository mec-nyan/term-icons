#include "niceties.h"

const char hline_thin[]		  = "─";
const char hline_dotted[]	  = "┄";
const char hline_fat[]		  = "━";
const char hline_dotted_fat[] = "┅";
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

typedef struct {
	const char *hl, *vl, *tl, *tr, *bl, *br;
} BoxChars;

int put_border(WINDOW* win, BoxChars* style) {
	int height = getmaxy(win);
	int width  = getmaxx(win);

	// Draw top and bottom borders:
	for (int i = 1; i < width - 1; i++) {
		if (mvwaddstr(win, 0, i, style->hl) == ERR) {
			return ERR;
		}
		if (mvwaddstr(win, height - 1, i, style->hl) == ERR) {
			return ERR;
		}
	}
	// Draw the left and right borders:
	for (int i = 1; i < height - 1; i++) {
		if (mvwaddstr(win, i, 0, style->vl) == ERR) {
			return ERR;
		}
		if (mvwaddstr(win, i, width - 1, style->vl) == ERR) {
			return ERR;
		}
	}

	// Draw the corners:
	if (mvwaddstr(win, 0, 0, style->tl) == ERR) {
		return ERR;
	}
	if (mvwaddstr(win, 0, width - 1, style->tr) == ERR) {
		return ERR;
	}
	if (mvwaddstr(win, height - 1, 0, style->bl) == ERR) {
		return ERR;
	}
	if (mvwaddstr(win, height - 1, width - 1, style->br) == ERR) {
		return ERR;
	}

	return 0;
}

BoxChars sharp = {
	.vl = vline_thin,
	.hl = hline_thin,
	.tl = topleft_sharp,
	.tr = topright_sharp,
	.bl = botleft_sharp,
	.br = botright_sharp,
};

BoxChars rounded = {
	.vl = vline_thin,
	.hl = hline_thin,
	.tl = topleft_rounded,
	.tr = topright_rounded,
	.bl = botleft_rounded,
	.br = botright_rounded,
};

BoxChars dotted = {
	.vl = vline_dotted,
	.hl = hline_dotted,
	.tl = topleft_sharp,
	.tr = topright_sharp,
	.bl = botleft_sharp,
	.br = botright_sharp,
};

BoxChars dotted_rounded = {
	.vl = vline_thin,
	.hl = hline_thin,
	.tl = topleft_rounded,
	.tr = topright_rounded,
	.bl = botleft_rounded,
	.br = botright_rounded,
};

BoxChars fat = {
	.vl = vline_fat,
	.hl = hline_fat,
	.tl = topleft_fat,
	.tr = topright_fat,
	.bl = botleft_fat,
	.br = botright_fat,
};

BoxChars fat_dotted = {
	.vl = vline_dotted_fat,
	.hl = hline_dotted_fat,
	.tl = topleft_fat,
	.tr = topright_fat,
	.bl = botleft_fat,
	.br = botright_fat,
};

BoxChars _double = {
	.vl = vline_double,
	.hl = hline_double,
	.tl = topleft_double,
	.tr = topright_double,
	.bl = botleft_double,
	.br = botright_double,
};

int sharp_box(WINDOW* win) {
	return put_border(win, &sharp);
}

int rounded_box(WINDOW* win) {
	return put_border(win, &rounded);
}

int dotted_box(WINDOW* win) {
	return put_border(win, &dotted);
}

int dotted_rounded_box(WINDOW* win) {
	return put_border(win, &dotted_rounded);
}

int fat_box(WINDOW* win) {
	return put_border(win, &fat);
}

int fat_dotted_box(WINDOW* win) {
	return put_border(win, &fat_dotted);
}

int double_box(WINDOW* win) {
	return put_border(win, &_double);
}
