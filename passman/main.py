#!/usr/bin/env python
# -*- coding: utf-8 -*-

from passman.enc import (encrypt, decrypt, decrypt_items_list, input_password)
from passman.menus import *
from passman.colors import FCOLOR_RED, COLOR_RESET, errprint, sucprint
from getpass import getpass
import passman.db as db
import pyperclip as pc
import signal
import sys
import argparse

TOKEN = b'D5-Xm4A4x9copCmwcp6MMcLAnOIgQJVDFmDJmkQYvT4='
conn = db.connect()


def exit_handler(signum=0, frame=0):
    conn.close()
    errprint("\nGood Bye.")
    exit(0)


def add_new_service(service: str, username: str, password: str):
    username = encrypt(TOKEN, username)
    password = encrypt(TOKEN, password)

    db.commit_service(conn, service, username, password)


def search_service(service: str):
    res = db.fetch_service(conn, service)

    return decrypt_items_list(TOKEN, (res, ))


def menu_interface():
    try:
        while (True):
            clear()
            option = dashboard_menu()

            if option == OPT_EXIT:
                return 0

            elif option == OPT_NEW:
                try:
                    service, username, password = new_service_menu()
                    pause()

                except PasswordConfirmationError:
                    errprint("Passwords don't match.")
                    pause()
                    continue

                try:
                    add_new_service(service, username, password)
                except ServiceAlreadyExists:
                    errprint("Service already exists.")
                    errprint(
                        f"Delete it using `{sys.argv[0]} -d {args.service}`.")
                    return 1

            elif option == OPT_SEARCH:
                service = input("Enter the service name: ")
                try:
                    items = search_service(service)
                    items_list_menu(items)
                    pc.copy(items[0][2])
                    pause()

                except ServiceNotFound:
                    errprint("Service not found.")

            elif option == OPT_ALL:
                items_list = db.fetch_all(conn)
                if not items_list: continue

                items_list = decrypt_items_list(TOKEN, items_list)
                items_list_menu(items_list)
                pause()

            elif option == OPT_DELETE:
                service = input("Enter the service name: ")
                try:
                    db.delete_service(conn, service)
                except ServiceNotFound:
                    errprint("Service not found.")

                pause()

    except Exception as e:
        errprint(f"Error: {e}")
        return 1

    return 0


def args_init():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--new", help="add a new service.")
    parser.add_argument("-u",
                        "--username",
                        help="username for the new service.")
    parser.add_argument("-s",
                        "--service",
                        help="get a stored password of a service.")
    parser.add_argument("-v",
                        "--visable",
                        action="store_true",
                        help="print output.")
    parser.add_argument("-d", "--delete", help="delete a service.")

    return parser.parse_args()


def args_interface(args):
    if args.service:
        try:
            res = search_service(args.service)
            res = res[0]
            if args.visable:
                print_service(*res)
                pc.copy(res[2])

            else:
                print_service(
                    res[0], res[1], FCOLOR_RED +
                    "Password has been copied to clipboard." + COLOR_RESET)

                pc.copy(res[2])

        except ServiceNotFound:
            errprint("Service not found.")
            print(f"Use `{sys.argv[0]} -n {args.service}` to add it.")
            return 1

    elif args.new:
        if not args.username:
            errprint("Please provide a username using `-u <username>`.")
            return 1

        try:
            args.password = input_password()
        except PasswordConfirmationError:
            errprint("Passwords don't match.")
            return 1

        try:
            add_new_service(args.new, args.username, args.password)
            sucprint("Service has been added successfully.")

        except PasswordConfirmationError:
            errprint("Passwords don't match.")
            return 1

        except ServiceAlreadyExists:
            errprint("Service already exists.")
            errprint(f"Delete it using `{sys.argv[0]} -d {args.service}`.")
            return 1

    elif args.delete:
        try:
            db.delete_service(conn, args.delete)
            sucprint("Service has been deleted successfully.")
        except ServiceNotFound:
            errprint("Service not found.")
            return 1

    return 0


def authenticate():
    master_password = db.fetch_pass(conn, "MASTER")
    password = getpass("Master password: ")
    master_password = decrypt(TOKEN, master_password)
    if password != master_password: raise AuthenticationFaild


def main():
    exit_stat = 0
    args = args_init()
    signal.signal(signal.SIGINT, exit_handler)
    db.create_tables(conn)
    try:
        authenticate()
    except AuthenticationFaild:
        errprint("Not a valid master password.")
        return 1
    except PasswordNotFound:
        infoprint(
            "You don't have a master password, Please set a master password.")
        try:
            password = input_password()
        except PasswordConfirmationError:
            errprint("Passwords don't match.")
            return 1

        add_new_service("MASTER", "MASTER", password)

    if len(sys.argv) > 1: exit_stat = args_interface(args)
    else: exit_stat = menu_interface()

   return exit_stat
