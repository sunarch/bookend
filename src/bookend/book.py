#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# previous license:
# Copyright (c) 2016 Anthony Pizzimenti - The MIT License (MIT)

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import json
import os
from termcolor import colored


class Book:

    def __init__(self):

        self.title = input('Title: ')
        self.author = input('Author: ')
        self.callnumber = input('Call Number: ')
        self.booklist = input('List Name: ')

    @staticmethod
    def formatbook(book, param=None):

        title = colored(book['title'], 'green') if param == 'title' else book['title']
        author = colored(book['author'], 'green') if param == 'author' else book['author']
        booklist = colored(book['booklist'], 'green') if param == 'booklist' else book['booklist']

        formatted = f'''
        Title:\t\t{title}
        Author:\t\t{author}
        Call Number:\t{book["callnumber"]}
        List:\t\t{booklist}
        '''

        return formatted


class BookEncoder:

    def __init__(self):
        self.collection = None
        self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lists.json')

    def encode(self, book=None):

        books = {}

        with open(self.path, 'r', encoding='UTF-8') as fh_list:

            try:
                books = json.loads(fh_list.read())
                books['books'].append(book)
            except KeyError or ValueError:
                print('There was an error reading the list file.')

        with open(self.path, 'w', encoding='UTF-8') as fh_list:

            try:
                fh_list.write(json.dumps(books))
            except:
                print('There was an error writing to the list file.')

    def encodecollection(self):

        with open(self.path, 'w', encoding='UTF-8') as fh_list:

            replace = {
                'books': self.collection
            }

            fh_list.write(json.dumps(replace))

    def decode(self):

        # opens list file and reads each book out of it
        with open(self.path, 'r', encoding='UTF-8') as fh_list:

            try:
                self.collection = json.loads(fh_list.read())['books']
            except ValueError:
                print('\nThe file\'s empty! You have no books.\n')
            finally:
                if not self.collection:
                    self.collection = []

    def remove(self, title):

        self.decode()

        for i, book in enumerate(self.collection):

            if title == book['title']:
                self.collection.pop(i)

        self.encodecollection()