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
	C.addstr(cs)
	C.free(unsafe.Pointer(cs))
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
