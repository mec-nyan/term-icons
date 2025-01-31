# Term icons

Easily find icons in your iconic font and use them in your Go programs.

> [!WARNING]
> This package is in an early stage of development!
> Nevertheless, you can stick to a version and use it. The icons packages won't change that much (or nothing at all).

## Usage

You can `go get` it _(use a specific version if you wish so)._

```sh
$ go get github.com/mec-nyan/term-icons/pkg/all@latest
```

Or just import it and let `go mod tidy` take care of it:

```go
package main

import "fmt"
import "github.com/mec-nyan/term-icons/pkg/all"

func main() {
	fmt.Printf("I love icons %c !!!\n", all.NfCod_HeartFilled)
}

```

Run it:

```
$ go run .
I love icons  !!!
```

## Search the desired icon:

To search for icons on your terminal, use the "./script/main.py" program provided.
It's just a simple program and it still needs a lot of work, but it works. I'm currently working on making a decent program out of it.

Please check the README in the `script` folder for more details.

![Screenshot](./script/screenshot_early_dev.png)

## TODO:

A lot!

But first: I've provided a pkg with all the consts (over 10K LOC...) and I've also provided smaller
packages grouping icons, so you just import the group you need (i.e. all FA icons). I've used
abbreviated names for those, so I need to give those packages a proper name.
