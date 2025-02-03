IN = main.c niceties.c
OUT = main.o
CFLAGS = -I/opt/homebrew/opt/ncurses/include -L/opt/homebrew/opt/ncurses/lib --std=c17 -Wall -lncurses

$(OUT): $(IN)
	@clang -o $(OUT) $(CFLAGS) $(IN)

run: $(OUT)
	@if [ -f $(OUT) ]; then ./$(OUT); fi
	@if [ -f $(OUT) ]; then rm $(OUT); fi
