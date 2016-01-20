#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys


sys.path.append(os.curdir)

SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = '/output/'

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
TRAVIS_CI_BADGE = "https://travis-ci.org/Hernrup/hernrup_se_colors.svg?branch=master"