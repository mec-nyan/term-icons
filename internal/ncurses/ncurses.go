package ncurses

import (
	"errors"
	"unsafe"
)

// #cgo LDFLAGS: -lcurses
// #include <stdlib.h>
// #include<locale.h>
// #include <curses.h>
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

func InitScr() {
	C.initscr()
}

func AddStr(s string) {
	cs := C.CString(s)
	defer C.free(unsafe.Pointer(cs))
	C.addstr(cs)
}

func Move(y, x int) {
	C.move(C.int(y), C.int(x))
}

func Refresh() {
	C.refresh()
}

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

func GetCh() byte {
	return byte(C.getch())
}

func EndWin() {
	C.endwin()
}

func ScreenSize() (int, int) {
	return int(C.LINES), int(C.COLS)
}

// Windows

// Encapsulate the C.WINDOW* here:
type Window struct {
	win           *C.WINDOW
	Height, Width int
	Y, X          int
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

func Box(w Window) {
	C.box(w.win, 0, 0)
}

func RoundedBox(w Window) {
	topleft := "╭"
	botleft := "╰"
	topright := "╮"
	botright := "╯"
	C.box(w.win, 0, 0)
	WMove(w, 0, 0)
	WAddStr(w, topleft)

	WMove(w, 0, w.Width-1)
	WAddStr(w, topright)

	WMove(w, w.Height-1, 0)
	WAddStr(w, botleft)

	WMove(w, w.Height-1, w.Width-1)
	WAddStr(w, botright)
}

func WAddStr(w Window, s string) {
	cs := C.CString(s)
	defer C.free(unsafe.Pointer(cs))
	C.waddstr(w.win, cs)
}

func WMove(w Window, y, x int) {
	C.wmove(w.win, C.int(y), C.int(x))
}

func WRefresh(w Window) {
	C.wrefresh(w.win)
}

func WGetCh(w Window) byte {
	return byte(C.wgetch(w.win))
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

func SetPair(w Window, pair int) {
	C.wattron(w.win, C.COLOR_PAIR(C.int(pair)))
}
