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
