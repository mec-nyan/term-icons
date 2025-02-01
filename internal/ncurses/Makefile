IN = main.c niceties.c
OUT = main.o
CFLAGS = --std=c17 -Wall -lncurses

$(OUT): $(IN)
	@gcc -o $(OUT) $(CFLAGS) $(IN)

run: $(OUT)
	@if [ -f $(OUT) ]; then ./$(OUT); fi
