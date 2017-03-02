#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pkg_resources import get_distribution

release = get_distribution('{{cookiecutter.module }}').version
version = '.'.join(release.split('.')[:2])

extensions = ['sphinx.ext.mathjax']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = '{{cookiecutter.module}}'
copyright = '2017, {{cookiecutter.author}}'
author = '{{cookiecutter.author }}'
language = None


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False


html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = '{{cookiecutter.module}}doc'

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
# epub_identifier = ''
# epub_uid = ''
epub_exclude_files = ['search.html']
