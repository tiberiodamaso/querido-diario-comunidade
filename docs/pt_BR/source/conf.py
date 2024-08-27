# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
from datetime import datetime

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Querido Diário"
copyright = f"2021–{datetime.now().year}, Open Knowledge Brasil"
author = "Open Knowledge Brasil"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "pt_BR"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# If true, Sphinx will warn about all references where the target cannot be 
# found. Default is False. 
nitpicky = True

# -- Options for HTML output -------------------------------------------------

html_build_dir = os.environ.get('READTHEDOCS_OUTPUT', 'docs/pt_BR/build/html')

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'analytics_id': 'G-X0VTXQ7XR3',
    'analytics_anonymize_ip': False, 
    'collapse_navigation': False,
    'logo_only': True,
    'style_nav_header_background': "#5e3f8e",
}

# A list of paths that contain custom _static files (such as style sheets or 
# script files). Relative paths are taken as relative to the configuration 
# directory
html_static_path = ['../../_static']

# The style sheet to use for HTML pages. A file of that name must exist either 
# in Sphinx’s _static/ path, or in one of the custom paths given in 
# html_static_path. Default is the stylesheet given by the selected theme. If 
# you only want to add or override a few things compared to the theme’s 
# stylesheet, use CSS @import to import the theme’s stylesheet.
html_style = 'css/custom.css'

# A list of CSS files. The entry must be a filename string or a tuple containing
# the filename string and the attributes dictionary.
#
html_css_files = ['custom.css']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = "../../_static/qd_logo_roxo.png"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "../../_static/favicon.ico"

# Language to be used for generating the HTML full-text search index.
html_search_language = 'pt'

