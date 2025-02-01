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

func main() {
	loc, err := SetLocale(LC_ALL, "en_US.UTF-8")
	if err != nil {
		panic(err)
	}

	stdscr := InitScr()
	Cbreak()
	NoEcho()

	defer Clean()

	if !HasColours() {
		return
	}

	StartColour()
	UseDefaultColours()
	InitPair(1, 212, -1)

	// NOTE: I may remove the non-qualified versions of "Move", "AddStr", etc.
	stdscr.Move(2, 8)
	stdscr.AddStr(fmt.Sprintf("Term size is %d lines x %d cols", stdscr.Height, stdscr.Width))
	stdscr.GetCh()

	stdscr.Move(4, 8)
	stdscr.AddStr("Locale set to: ")
	stdscr.AddStr(loc)

	stdscr.Move(5, 8)
	stdscr.AddStr("> ")
	x := stdscr.GetCh()
	stdscr.AddStr("*")

	stdscr.Move(6, 8)
	stdscr.AddStr("Got: ")
	stdscr.AddStr(fmt.Sprintf("%c", x))

	stdscr.Move(7, 8)
	stdscr.AddStr("> ")

	buff := []byte{}
	for {
		y := stdscr.GetCh()
		if y == '\n' {
			break
		}
		stdscr.AddStr("*")
		buff = append(buff, y)
	}

	stdscr.Move(8, 8)
	stdscr.AddStr("Got: ")
	stdscr.AddStr(string(buff))

	stdscr.Move(9, 8)
	stdscr.AddStr("> (next) ")

	stdscr.GetCh()
	stdscr.Clear()
	stdscr.Refresh()

	win := NewWin(3, 20, 0, 0)
	win.SetPair(1)
	win.RoundedBox()
	win.Move(1, 1)
	win.GetCh()
	win.Move(1, 1)
	win.AddStr(fmt.Sprintf("WinSize: %d x %d", win.Height, win.Width))
	win.GetCh()
}

func Clean() {
	Echo()
	NoCbreak()
	EndWin()
}
