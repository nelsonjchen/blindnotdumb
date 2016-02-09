#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#THEME = 'pelican-themes/blueidea/'
THEME = 'pelican-themes/alchemy/alchemy/'

AUTHOR = u'Chris Patti'
SITENAME = u'Blind Not Dumb'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

TAGS_ON_MENU = True
CATEGORIES_ON_MENU = True
ARCHIVES_ON_MENU = True
PAGES_ON_MENU = True
PROFILE_IMAGE = 'images/profile_pic.jpg'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
LINKS = (('Podcast.__init__', 'http://www.podcastinit.com/'),
         ('Empiricism Ops', 'https://danslimmon.wordpress.com/'),
         ('AJS Essays', 'http://essays.ajs.com/'),)

# Social widget
SOCIAL = (('Me @ Everywhere :)', 'http://about.me/feoh'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TWITTER_ADDRESS='feoh'
GITHUB_ADDRESS='http://www.github.com/feoh'
EMAIL_ADDRESS='cpatti@gmail.com'
