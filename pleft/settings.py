# -*- coding: utf-8 -*-

# Copyright 2010 Sander Dijkhuis <sander.dijkhuis@gmail.com>
#
# This file is part of Pleft.
#
# Pleft is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pleft is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pleft. If not, see <http://www.gnu.org/licenses/>.

# Django settings for Pleft.

import os

from plapp.settings_common import *
from local_settings import *

TEMPLATE_DEBUG = DEBUG

SITE_NAME = 'blim'

ALPHA = False

ADMINS = (
    ('blim', 'blimserver@blim.net'),
)

MANAGERS = ADMINS

SITE_BASE = 'http://' +  SITE_DOMAIN

STATIC_URL = '/static/'

LANGUAGE_CODE = 'en'
USE_I18N = True

LANGUAGES = (
    ('en', 'English'),
    ('fr', 'Français'),
    ('de', 'Deutsch'),
    ('es_ES', 'Español'),
    ('it', 'Italiano'),
    ('nl', 'Nederlands'),
    ('ru', 'Русский'),
)

ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

ABUSE_EMAIL = 'jc@blim.net'
MAIL_SENDER = 'blimserver<jc@blim.net>'

EMAIL_LOGO = SITE_BASE + '/static/site/images/mail-logo.png'
EMAIL_INFO = 'jc@blim.net'

SCREENSHOT = SITE_BASE + '/static/images/thumbnail.png'
