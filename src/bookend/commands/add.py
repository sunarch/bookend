#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser

# imports: project
from bookend import book
from bookend import book_list


COMMAND_ADD = 'add'


def subparser_add(subparsers):
    _: ArgumentParser = subparsers.add_parser(COMMAND_ADD)


def processor_add(data: dict, _):

    book_item = book.input_book()
    book_list.add_book(data, book_item)

    to_save = True
    return data, to_save
