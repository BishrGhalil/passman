#!/usr/bin/env python
# -*- coding: utf-8 -*-

COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"

FCOLOR_RED = "\033[91m"
FCOLOR_GREEN = "\033[92m"
FCOLOR_YELLOW = "\033[93m"
FCOLOR_BLUE = "\033[94m"
FCOLOR_HEADER = "\033[95m"
FCOLOR_CYAN = "\033[96m"

FCOLORS_LIST = [
    FCOLOR_BLUE,
    FCOLOR_GREEN,
    FCOLOR_YELLOW,
    FCOLOR_CYAN,
]

def errprint(msg: str):
    print(FCOLOR_RED + msg + COLOR_RESET)

def sucprint(msg: str):
    print(FCOLOR_GREEN + msg + COLOR_RESET)

def infoprint(msg: str):
    print(FCOLOR_BLUE + msg + COLOR_RESET)

def warprint(msg: str):
    print(FCOLOR_YELLOW + msg + COLOR_RESET)
