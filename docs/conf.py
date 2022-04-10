# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sphinx_py3doc_enhanced_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'seldom'
year = '2015-2022'
author = 'bugmaster'
copyright = '{0}, {1}'.format(year, author)
version = release = '2.6.0'

pygments_style = 'trac'
templates_path = ['.']

html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/SeldomQA/seldom',
    'appendcss': '''
        div.body code.descclassname { display: none }
        div.body #pedantic-mode code.descclassname { display: inline-block }
    ''',
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
