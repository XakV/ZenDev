#!/usr/bin/python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Zach Villers'
SITENAME = 'thought packets'
SITEURL = 'https://zenacity.org'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

PATH = 'content'
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/')
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/XakV'),
          ('Pagure.io', 'https://pagure.io/user/aikidouke'),
          ('Fedora - Aikidouke', 'https://admin.fedoraproject.org/accounts/user/view/aikidouke'),
          ('Fosstodon.org - Denderix', 'https://fosstodon.org/web/accounts/45241'))

DEFAULT_PAGINATION = 10

# Theme Config
import bulrush
THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

PLUGIN_PATHS = 'plugins'
PLUGINS = ['assets']
