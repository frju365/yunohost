# -*- coding: utf-8 -*-

""" License

    Copyright (C) 2013 YunoHost

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program; if not, see http://www.gnu.org/licenses

"""

""" yunohost_theme.py

    Manage themes
"""

import os
import json
import yaml
import time
import re
import urlparse
import subprocess
import glob
import pwd
import grp
from collections import OrderedDict
from datetime import datetime

from moulinette import msignals, m18n, msettings
from yunohost.utils.error import YunohostError
from moulinette.utils.log import getActionLogger
from moulinette.utils.filesystem import read_json


themedir = '/etc/ssowat/portal/assets/themes/'

def theme_listlists():
    try:
        files = [f for f in listdir(themedir) if isfile(join(themedir, f))]
        pass
    except Exception as e:
        raise

    return files

def theme_list():

def themeremove(theme=null)
    if theme is null:
        logg
