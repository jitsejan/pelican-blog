#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Jitse-Jan'
SITENAME = u"JJ's World"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = 'themes/middle-theme'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['liquid_tags.notebook', 'liquid_tags.literal']

DELETE_OUTPUT_DIRECTORY = False
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8') if os.path.exists('_nb_header.html') else None
NOTEBOOK_DIR = 'notebooks'
LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'jqadrad'

TYPOGRIFY = True
PAGE_PATHS = ['pages']
PAGES = [{'url': 'pages/latex-cheatsheet', 'title': 'Latex cheatsheet'},
		 {'url': 'pages/pandas-cheatsheet', 'title': 'Pandas cheatsheet'},
		 {'url': 'pages/python-cheatsheet', 'title': 'Python cheatsheet'},
		 {'url': 'pages/splunk-cheatsheet', 'title': 'Splunk cheatsheet'},
		]