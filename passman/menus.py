#!/usr/bin/env python
# -*- coding: utf-8 -*-

from passman.colors import *
from passman.exceptions import *
import random
import os
import sys

passman_logo = rf"""
{FCOLOR_BLUE} ____               {FCOLOR_RED}  __  __             
{FCOLOR_BLUE}|  _ \ __ _ ___ ___ {FCOLOR_RED} |  \/  | __ _ _ __  
{FCOLOR_BLUE}| |_) / _` / __/ __ {FCOLOR_RED} | |\/| |/ _` | '_ \ 
{FCOLOR_BLUE}|  __/ (_| \__ \__ \{FCOLOR_RED} | |  | | (_| | | | |
{FCOLOR_BLUE}|_|   \__,_|___/___/{FCOLOR_RED} |_|  |_|\__,_|_| |_|

By: Beshr Ghalil
Versoin: 2.0
"""

logo = f"""{FCOLOR_BLUE}{passman_logo}{COLOR_RESET}"""


def sep():
    return print("-" * 10)


def clear():
    return os.system("clear")


OPT_NEW = '1'
OPT_SEARCH = '2'
OPT_ALL = '3'
OPT_DELETE = '4'
OPT_EXIT = '5'
OPT_UNKOWN = '\0'
PROMPT = ">>> "

try:
    from msvcrt import getch
except ImportError:
    import tty
    import termios

    def getch():
        """Gets a signle character from STDIO."""
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    def pause(msg: str = "Press any key to continue."):
        print(msg)
        getch()


def dashboard_menu():

    msg = f"""
{FCOLOR_RED}"Choose an option"{COLOR_RESET}
    {FCOLOR_BLUE}1) Enter a new password
    2) Search
    3) View all
    4) Delete
    {FCOLOR_RED}5) Exit{COLOR_RESET}
"""

    print(logo)
    print(msg)
    option = getch()
    return option


def print_service(service, username, password):
    color = random.choice(FCOLORS_LIST)
    print(f"{color}", end="")
    print(f"Service: {service}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"{COLOR_RESET}", end="")


def items_list_menu(items_list):
    for index, data in enumerate(items_list):
        service = data[0]
        username = data[1]
        password = data[2]

        print(f"{index + 1}:")
        sep()
        print_service(service, username, password)


def new_service_menu():
    service = input("Enter the service name: ")
    username = input("Enter a username for this service: ")
    password = input_password()

    return (service, username, password)
