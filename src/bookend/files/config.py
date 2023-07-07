#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import json
import logging
import os.path
import shutil

# imports: dependencies
from xdg_base_dirs import xdg_config_home

# imports: project
from bookend import version


def _config_dir_path() -> str:
    config_dir_path = os.path.join(xdg_config_home(), version.PROGRAM_NAME)

    if not os.path.isdir(config_dir_path):
        os.makedirs(config_dir_path, mode=0o740, exist_ok=True)

    return config_dir_path


def _config_file_name() -> str:
    return f'{version.PROGRAM_NAME}.json'


def _config_file_path() -> str:
    config_file_path = os.path.join(_config_dir_path(), _config_file_name())

    if not os.path.isfile(config_file_path):
        with open(config_file_path, 'w', encoding='UTF-8') as fh_config:
            json.dump(default_config(), fh_config, indent=2)
        logging.info('Created new config at "%s"', config_file_path)

    return config_file_path


def load() -> dict:
    config_file_path = _config_file_path()

    with open(_config_file_path(), 'r', encoding='UTF-8') as fh_config:
        logging.info('Loaded config from "%s"', config_file_path)
        return json.load(fh_config)


def save(config: dict) -> None:
    config_file_path = _config_file_path()
    backup_file_path = f'{_config_file_path()}.bak'

    shutil.copy2(_config_file_path(), f'{config_file_path}.bak')
    logging.info('Backed up config to "%s"', backup_file_path)

    with open(_config_file_path(), 'w', encoding='UTF-8') as fh_config:
        logging.info('Saved config to "%s"', config_file_path)
        json.dump(config, fh_config, indent=2)


def default_config() -> dict:
    return {}
