#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser
import configparser
import logging
import logging.config
import pkg_resources

# imports: project
from bookend import version
from bookend import arg_handler
from bookend import book_list


def main() -> None:

    logger_config_name = 'data/logger.ini'

    if not pkg_resources.resource_exists(__name__, logger_config_name):
        logging.error('logger config does not exist')
        return

    logger_config = pkg_resources.resource_stream(__name__, logger_config_name)
    logger_config_str = logger_config.read().decode('UTF-8')
    logger_config_parser = configparser.ConfigParser()
    logger_config_parser.read_string(logger_config_str)
    logging.config.fileConfig(logger_config_parser)

    logging.info(version.PROGRAM_NAME)
    logging.info('-' * len(version.PROGRAM_NAME))

    parser = ArgumentParser(prog=version.PROGRAM_NAME)

    parser.add_argument(
        '-v', '--version',
        help='Display version',
        action='store_true',
        dest='version'
    )

    option_group = parser.add_mutually_exclusive_group()

    option_group.add_argument(
        '-s', '--search', metavar='TERM',
        help='search for a term across all lists',
        dest='search', default=None
    )

    option_group.add_argument(
        '-l', '--list',
        help='prints a list of booklists',
        action='store_true',
        dest='list'
    )

    option_group.add_argument(
        '-a', '--add',
        help='add a new book!',
        action='store_true',
        dest='add'
    )

    option_group.add_argument(
        '-c', '--checkout', metavar='TITLE',
        help='enter the title of a book, and it\'ll be removed from the list',
        dest='checkout', default=None
    )

    args = parser.parse_args()

    book_list_path = book_list.list_file_path()
    book_list.init(book_list_path)

    if args.version:
        print(f'{version.PROGRAM_NAME} {version.__version__}')
        return

    if args.search is not None:
        arg_handler.arg_search(book_list_path, args.search)

    if args.list:
        arg_handler.arg_list(book_list_path)

    if args.add:
        arg_handler.arg_add(book_list_path)

    if args.checkout is not None:
        arg_handler.arg_checkout(book_list_path, args.checkout)


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------- #
