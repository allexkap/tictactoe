PYTHON=$(VENV)/bin/python3
CC=gcc

.PHONY: all clean


all: tictactoe.c
	$(CC) -o tictactoe tictactoe.c

tictactoe.c: codegen.py
	$(PYTHON) codegen.py

clean:
	rm -f tictactoe tictactoe.c
