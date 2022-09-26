#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = "ANKiTC"
SITENAME = "Anaesthesia Network for Kidney Transplantation in Children"
SITENAME_SHORT = "ankitc"
SITE_REPO = "website-ankitc"
SITE_GROUP = "ankitc"

# Home page and social settings
SITETITLE = "Anaesthesia Network for Kidney Transplantation in Children"
SITELEAD = """
This workgroup aims to improve perioperative care in paediatric kidney transplantation.
"""
SITE_PICTURE = "images/general/AI4A.jpeg"

HOME_IMAGE = None #"images/general/AI4A.jpeg"
HOME_IMAGE_CAPTION = ''

TWITTER_URL = None
FOOTER_TEXT = ""
TOP_DOMAIN = ''
PARENT_DOMAIN = (
    ''
)
HOME_JUMBOTRON_LAYOUT = "neural-bg"

# Whether to show email buttons on every person circle
SHOW_EMAIL_GROUP_MEMBERS_INLINE = False

# What sections to show in the nav bar
NAV_SECTIONS = [
    {"name": "About", "url": "about", "icon_mobile": "info", "text_class": "d-lg-block"},
    {"name": "Members", "url": "members", "icon_mobile": "users", "text_class": "d-lg-block"},
    #{"name": "Research", "url": "research", "icon_mobile": "folder"},
    #{"name": "Highlights", "url": "highlights", "icon": "megaphone"},
    #{"name": "Members", "url": "members", "icon": "users"},
    {"name": "Research", "url": "projects", "icon_mobile": "folder"},
    #{"name": "Vacancies", "url": "vacancies", "icon_mobile": "vacancies"},
    {"name": "Publications", "url": "publications", "icon_mobile": "file-text-o"},
    #{"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon_mobile": "envelope-o", "text_class": "d-lg-block"},
]

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {
    "News": "News",
    "Projects": "Projects",
}

# URLs
SITEURL = "https://www.ankitc.eu"
IMGURL = SITEURL
EDIT_CONTENT_URL = (
    "https://github.com/RobTolboom/ankitc-website/edit/master/{file_path}"
)

#
# Non-content variables
# In general these values do not have to be changed.
#
PATH = "content"
RELATIVE_URLS = False

# Show pdf request on publication pages
ENABLE_PUBLICATION_PDF_REQUEST = False

TIMEZONE = "Europe/Amsterdam"
DEFAULT_LANG = "EN"
ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CURRENTYEAR = date.today().year
TODAY = date.today()
LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = "content/dict_pubs.json"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
SLUGIFY_SOURCE = "basename"

ARTICLE_URL = "news/{slug}/"
ARTICLE_SAVE_AS = "news/{slug}/index.html"
ARTICLE_TYPE = "News"

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

ARCHIVES_SAVE_AS = ""
SITEMAP_SAVE_AS = "sitemap.xml"
INDEX_SAVE_AS = "news/index.html"

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ["index", "sitemap"]

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = [
    "bibtex",
    "bibtex_loader",
    "edit_url",
    "hierarchy",
    "fileutil",
    "bootstrapify",
    "imgutil",
    "inline_extend",
    "content_aggregator",
]
