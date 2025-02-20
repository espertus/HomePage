# -*- coding: utf-8 -*-

# flake8: noqa

import tinkerer
import tinkerer.paths

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = "Runestone Academy"

# Change this to the tagline of your blog
tagline = "Democratizing textbooks for the 21st century"

# Change this to the description of your blog
description = "Interactive Textbooks for Computer Science, Data Science and more"

# Change this to your name
author = "Brad Miller"

# Change this to your copyright string
copyright = "2022, " + author

# Change this to your blog root URL (required for RSS feed)
website = "http://www.runestoneinteractive.com/"

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = "runestoneblog"

# Change your favicon (new favicon goes in _static directory)
html_favicon = "_static/runestone.ico"

# Pick another Tinkerer theme or use your own
# html_theme = 'modern5'
html_theme = "runestone"

# Theme-specific options, see docs
html_theme_options = {}

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None

# Generate full posts for RSS feed even when using "read more"
rss_generate_full_posts = False

# Number of blog posts per page
posts_per_page = 10

# Character use to replace non-alphanumeric characters in slug
slug_word_separator = "_"

# Set to page under /pages (eg. "about" for "pages/about.html")
landing_page = None

# Set to override the default name of the first page ("Home")
first_page_title = None

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ["tinkerer.ext.blog", "tinkerer.ext.disqus", "sphinx_reredirects"]

redirects = {"pages/library": "https://runestone.academy/ns/books/index"}

# Add other template paths here
templates_path = ["_templates"]

# Add other static paths here
html_static_path = ["_static", tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ["_themes", tinkerer.paths.themes]

# Add file patterns to exclude from build
exclude_patterns = ["drafts/*", "_templates/*", "README.rst", ".history/*"]

# Add templates to be rendered in sidebar here
html_sidebars = {
    "**": [
        "recent.html",
        "runestone_academy.html",
        "runestone_links.html",
        "partners.html",
        "searchbox.html",
        "support.html",
        "categories.html",
    ]
}

# Add an index to the HTML documents.
html_use_index = False

# **************************************************************
# Do not modify below lines as the values are required by
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_show_sourcelink = False
html_add_permalinks = ""
