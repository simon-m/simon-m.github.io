#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Simon-M.'
SITENAME = u'Weblog'
SITETITLE = 'What\'s in there?'
SITESUBTITLE = "Random notes about data analysis at large"
SITEDESCRIPTION = ('Notes and ressources about '
		   'data analysis, machine learning, '
		   'statistics and epidemiology')

SITEURL = 'index.html'
PATH = 'content'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (('Categories', 'categories.html'),
            ('Tags', 'tags.html'),)

# Blogroll
# LINKS =  (('Home', 'index.html'),
        # ('Categories', 'categories.html'),
        # ('Tags', 'tags.html'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

COPYRIGHT_YEAR = 2017

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False

THEME_STATIC_DIR = "themes"
THEME = "themes/Flex"
GITHUB_URL = "https://github.com/simon-m"


