#include <curses.h>

// Draw a border for the WINDOW with rounded corners.
int rounded_box(WINDOW* win);

// Draw a border for the WINDOW with sharp corners.
int sharp_box(WINDOW* win);

// Draw a border for the WINDOW with sharp corners and dotted lines.
int dotted_box(WINDOW* win);

// Draw a border for the WINDOW with rounded corners and dotted lines.
int dotted_rounded_box(WINDOW* win);

// Draw a border for the WINDOW with fat lines.
int fat_box(WINDOW* win);

// Draw a border for the WINDOW with rounded corners.
int fat_dotted_box(WINDOW* win);

// Draw a border for the WINDOW with double lines.
int double_box(WINDOW* win);

// Write the text to the window, but dont break words.
// Obey new lines, use padding.
// Return the position of the last byte/character printed,
// in case that the text didn't fit the window.
int print(WINDOW* win, const char* text, int top, int right, int bot,
	int left);

typedef struct {
	int height, width;
} RectSize;

typedef struct {
	int y, x;
} RectPos;

typedef struct {
	RectSize ws;
	RectPos	 wp;
} Geometry;

typedef struct {
	const char *hl, *vl, *tl, *tr, *bl, *br;
} BorderStyle;

typedef struct {
	WINDOW*	 win;
	Geometry geom;
} Rect;

typedef struct {
	int top, right, left, bottom;
} Padding;

typedef struct {
	Rect		outer, inner;
	BorderStyle style;
} BorderedRect;

Rect new_rect(RectSize size, RectPos pos);
int	 rect_write(Rect* rect, const char* text);
void rect_refresh(Rect* rect);
void rect_clear(Rect* rect);

BorderedRect new_bordered_rect(RectSize size, RectPos pos, Padding pad, BorderStyle style);
int			 b_rect_border(BorderedRect* brect);
int			 b_rect_write(BorderedRect* brect, const char* text);
void		 b_rect_refresh(BorderedRect* brect);
void		 b_rect_clear(BorderedRect* rect);
int			 b_rect_title(BorderedRect* rect, int pos, int margin, const char* title);

extern BorderStyle border_sharp;

extern BorderStyle border_rounded;

extern BorderStyle border_dotted;

extern BorderStyle border_dotted_rounded;

extern BorderStyle border_fat;

extern BorderStyle border_fat_dotted;

extern BorderStyle border_double;
