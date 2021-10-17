all: install

install:
	cp passman /usr/bin/passman

uninstall:
	rm -rf /usr/bin/passman
