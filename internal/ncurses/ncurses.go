package ncurses

import (
	"errors"
	"unsafe"
)

// #cgo CFLAGS: -I/opt/homebrew/opt/ncurses/include --std=c17 -Wall
// #cgo LDFLAGS: -L/opt/homebrew/opt/ncurses/lib -lncurses
// #include <stdlib.h>
// #include <locale.h>
// #include <curses.h>
// #include "niceties.h"
import "C"

const (
	LC_ALL = iota
	LC_COLLATE
	LC_CTYPE
	LC_MONETARY
	LC_NUMERICS
	LC_TIME
)

func SetLocale(category int, locale string) (string, error) {
	var cat int
	switch category {
	case LC_ALL, LC_COLLATE, LC_CTYPE, LC_MONETARY, LC_NUMERICS, LC_TIME:
		cat = category
	default:
		return "", errors.New("Invalid category.")
	}

	cs := C.CString(locale)
	lc := C.GoString(C.setlocale(C.int(cat), cs))
	C.free(unsafe.Pointer(cs))

	if lc == "" {
		return "", errors.New("Couldn't set locale.")
	}

	return lc, nil
}

func GetNcursesVersion() (major, minor int) {
	version := C.get_ncurses_version()
	major = int(version.major)
	minor = int(version.minor)
	return
}

// Encapsulate the C.WINDOW* here:
type Window struct {
	win           *C.WINDOW
	Height, Width int
	Y, X          int
}

func InitScr() Window {
	// TODO: Check if "stdscr" is NULL.
	return Window{
		win:    C.initscr(),
		Height: int(C.LINES),
		Width:  int(C.COLS),
		Y:      0,
		X:      0,
	}
}

func NewWin(height, width, y, x int) Window {
	return Window{
		C.newwin(C.int(height), C.int(width), C.int(y), C.int(x)),
		height,
		width,
		y,
		x,
	}
}

// These can alse be used with "stdscr"!
func (w Window) Box() {
	C.box(w.win, 0, 0)
}

func (w Window) RoundedBox() {
	C.rounded_box(w.win)
}

func (w Window) AddStr(s string) {
	cs := C.CString(s)
	defer C.free(unsafe.Pointer(cs))
	C.waddstr(w.win, cs)
}

func (w Window) Move(y, x int) {
	C.wmove(w.win, C.int(y), C.int(x))
}

func (w Window) Refresh() {
	C.wrefresh(w.win)
}

func (w Window) GetCh() byte {
	return byte(C.wgetch(w.win))
}

func (w Window) Clear() {
	C.wclear(w.win)
}

// Some colours.
func HasColours() bool {
	return bool(C.has_colors())
}

func StartColour() {
	C.start_color()
}

func UseDefaultColours() {
	C.use_default_colors()
}

func InitPair(pair, fg, bg int) {
	C.init_pair(C.short(pair), C.short(fg), C.short(bg))
}

func(w Window) SetPair( pair int) {
	C.wattron(w.win, C.COLOR_PAIR(C.int(pair)))
}

// Just to keep consistency with curses, but these ones are nor really necessary.
// These are (in C) just macros that call a "w" function with "stdscr" as first argument.
func AddStr(s string) {
	cs := C.CString(s)
	defer C.free(unsafe.Pointer(cs))
	C.addstr(cs)
}

func GetCh() byte {
	return byte(C.getch())
}

func Move(y, x int) {
	C.move(C.int(y), C.int(x))
}

func Refresh() {
	C.refresh()
}

// Standalone curses functions.
func Cbreak() int {
	return int(C.cbreak())
}

func NoCbreak() int {
	return int(C.nocbreak())
}

func Echo() int {
	return int(C.echo())
}

func NoEcho() int {
	return int(C.noecho())
}

func EndWin() {
	C.endwin()
}

func ScreenSize() (int, int) {
	return int(C.LINES), int(C.COLS)
}
