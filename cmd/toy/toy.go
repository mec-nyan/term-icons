// A "Toy" program.
//
// This program is here only to try the wrapper around the ncurses C library.
// The ideea is to try out ideas and then make the "search.go" app using This
// same bindings. NCurses is fun!
package main

import (
	"fmt"

	. "github.com/mec-nyan/term-icons/internal/ncurses"
)

func main(){
	loc, err := SetLocale(LC_ALL, "en_US.UTF-8")
	if err != nil {
		panic(err)
	}
	InitScr()
	Cbreak()
	NoEcho()

	if HasColours() {
		StartColour()
		UseDefaultColours()
	}

	InitPair(1, 212, -1)

	win := NewWin(3, 20, 0, 0)
	SetPair(win, 1)
	RoundedBox(win)
	WMove(win, 1, 1)
	// WAddStr(win, "ima window!")
	WGetCh(win)
	WMove(win, 1, 1)
	WAddStr(win, fmt.Sprintf("WinSize: %d x %d", win.Height, win.Width))
	WGetCh(win)

	height, width := ScreenSize()
	Move(2, 8)
	AddStr(fmt.Sprintf("Term size is %d lines x %d cols", height, width))
	GetCh()

	Move(4, 8)
	AddStr("Locale set to: ")
	AddStr(loc)

	Move(5, 8)
	AddStr("> ")
	x := GetCh()
	AddStr("*")

	Move(6, 8)
	AddStr("Got: ")
	AddStr(fmt.Sprintf("%c", x))

	Move(7, 8)
	AddStr("> ")

	buff := []byte{}
	for {
		y := GetCh()
		if y == '\n' {
			break
		}
		AddStr("*")
		buff = append(buff, y)
	}

	Move(8, 8)
	AddStr("Got: ")
	AddStr(string(buff))

	Move(9, 8)
	AddStr("> (quit) ")

	GetCh()

	Echo()
	NoCbreak()
	EndWin()
}
