.PHONY: all clean


all: auto

auto: auto.c
	gcc -o auto auto.c

auto.c: gen.py
	python gen.py

clean:
	rm -f auto auto.c
