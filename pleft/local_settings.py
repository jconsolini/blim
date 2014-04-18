#coding=utf-8
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


DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '3306'
DATABASE_NAME = 'pleftdb'
DATABASE_USER = 'root'
DATABASE_PASSWORD = '00platypus'

SITE_DOMAIN = 'dev.blim.net'

DEBUG = True

EMAIL_HOST = 'smtp-relay.gmail.com'
#EMAIL_PORT = 25
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_FILE_PATH = '/TMP/EMAIL'

# Make this unique, and don't share it with anybody.
# Can be creating using the following command:
# python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])'
SECRET_KEY = 'gfadgfadgfdagfdagfda'

