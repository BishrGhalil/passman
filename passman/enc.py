#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet
from getpass import getpass
from passman.exceptions import *


def encrypt(token, string: str):
    fernet = Fernet(token)
    encString = fernet.encrypt(string.encode())
    return encString


def decrypt(token, encString):
    fernet = Fernet(token)
    decString = fernet.decrypt(encString).decode()
    return decString


def decrypt_items_list(token, items_list):
    new_list = []
    for data in items_list:
        service = data[0]
        username = decrypt(token, data[1])
        password = decrypt(token, data[2])
        new_list.append((service, username, password))

    return new_list


def input_password():
    password = getpass("Enter a password: ")
    confirm = getpass("Confirm your password: ")
    if password != confirm: raise PasswordConfirmationError
    else: return password
