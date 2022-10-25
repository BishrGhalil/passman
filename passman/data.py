#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DATA_DIR = ".passman"
PASSMAN_DIR = f"{os.path.join(os.getenv('HOME'), DATA_DIR)}"

DB_CREATION_SCRIPT = """
CREATE TABLE IF NOT EXISTS passwords(
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  SERVICE TEXT NOT NULL,
  USERNAME TEXT NOT NULL,
  PASSWD TEXT NOT NULL
);
"""
