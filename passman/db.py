#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os
from os import path
from passman.data import (PASSMAN_DIR, DB_CREATION_SCRIPT)
from passman.exceptions import *

DB_PATH = f"{path.join(PASSMAN_DIR, 'passman.db')}"


def connect():
    if not path.lexists(PASSMAN_DIR):
        os.mkdir(PASSMAN_DIR)
    else:
        conn = sqlite3.connect(DB_PATH)
        return conn


def create_tables(conn):
    cur = conn.cursor()
    cur.execute(DB_CREATION_SCRIPT)


def check_service(conn, service):
    cur = conn.cursor()
    data = (service, )
    query = "SELECT ID FROM passwords WHERE SERVICE = ?"
    res = cur.execute(query, data)
    res = cur.fetchone()

    if not res: return False
    return True


def commit_service(conn, service, username, password):
    if check_service(conn, service): raise ServiceAlreadyExists
    cur = conn.cursor()
    data = (service, username, password)
    query = "INSERT INTO passwords (SERVICE, USERNAME, PASSWD) VALUES (?, ?, ?)"
    cur.execute(query, data)
    conn.commit()


def fetch_service(conn, service):
    cur = conn.cursor()
    data = (service, )
    query = "SELECT SERVICE, USERNAME, PASSWD FROM passwords WHERE SERVICE = ?"
    res = cur.execute(query, data)

    res = cur.fetchone()
    if not res: raise ServiceNotFound
    return res


def fetch_username(conn, service):
    cur = conn.cursor()
    data = (service, )
    query = "SELECT USERNAME FROM passwords WHERE SERVICE = ?"
    res = cur.execute(query, data)

    if not res: raise UsernameNotFound
    res = cur.fetchone()
    return res[0]


def fetch_pass(conn, service):
    cur = conn.cursor()
    data = (service, )
    query = "SELECT PASSWD FROM passwords WHERE SERVICE=?"
    res = cur.execute(query, data)

    res = cur.fetchone()
    if not res: raise PasswordNotFound
    return res[0]


def fetch_all(conn):
    cur = conn.cursor()
    query = "SELECT SERVICE, USERNAME, PASSWD FROM passwords"
    res = cur.execute(query)

    if not res: return None
    res = res.fetchall()
    return res


def delete_service(conn, service):
    if not check_service(conn, service): raise ServiceNotFound
    cur = conn.cursor()
    data = (service, )
    query = "DELETE FROM passwords WHERE SERVICE = ?"
    cur.execute(query, data)
    conn.commit()

    return True
