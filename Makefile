PYTHON=$(VENV)/bin/python3
CC=gcc

.PHONY: all clean


all: auto

auto: auto.c
	$(CC) -o auto auto.c

auto.c: gen.py
	$(PYTHON) gen.py

clean:
	rm -f auto auto.c
