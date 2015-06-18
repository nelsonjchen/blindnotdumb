#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'pelican-themes/blueidea/'

AUTHOR = u'Chris Patti'
SITENAME = u'Blind Not Dumb'
SITEURL = 'http://www.feoh.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = True
CATEGORY_FEED_ATOM = True
TRANSLATION_FEED_ATOM = True
AUTHOR_FEED_ATOM = True
AUTHOR_FEED_RSS = True



# Blogroll
LINKS = (('I am one of the Co-hosts of Podcast.__init__', 'http://www.podcastinit.com/'),
         ('My good friend and lodge brother Aaron Sherman', 'http://essays.ajs.com/'),)


# Social widget
SOCIAL = (('Me @ Everywhere :)', 'http://about.me/feoh'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
