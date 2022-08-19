#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# previous license:
# Copyright (c) 2016 Anthony Pizzimenti - The MIT License (MIT)

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import os


def getlast(path):
    return path.split(os.pathsep)[-1]


def makefolder(path):
    os.makedirs(path)
    print("directory created at /{}".format(getlast(path)))


def makefile(path):
    file = open(path, "w")
    file.close()

    print("Created new list file at {}".format(getlast(path)))


def write(content, path="lists.json"):

    with open(path, "w") as file:
        file.write(content)
