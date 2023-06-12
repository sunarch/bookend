#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from bookend.commands.add import subparser_add, COMMAND_ADD, processor_add
from bookend.commands.checkout import subparser_checkout, COMMAND_CHECKOUT, processor_checkout
from bookend.commands.list import subparser_list, COMMAND_LIST, processor_list
from bookend.commands.search import subparser_search, COMMAND_SEARCH, processor_search


SUBPARSER_ADDERS = [
    subparser_add,
    subparser_checkout,
    subparser_list,
    subparser_search
]

PROCESSORS = {
    COMMAND_ADD: processor_add,
    COMMAND_CHECKOUT: processor_checkout,
    COMMAND_LIST: processor_list,
    COMMAND_SEARCH: processor_search
}

COMMANDS = PROCESSORS.keys()
