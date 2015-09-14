# -*- coding: utf-8 -*-
"""
    jinja2
    ~~~~~~

    Jinja2 is a template engine written in pure Python.  It provides a
    Django inspired non-XML syntax but supports inline expressions and
    an optional sandboxed environment.

    Nutshell
    --------

    Here a small example of a Jinja2 template::

        {% extends 'base.html' %}
        {% block title %}Memberlist{% endblock %}
        {% block content %}
          <ul>
          {% for user in users %}
            <li><a href="{{ user.url }}">{{ user.username }}</a></li>
          {% endfor %}
          </ul>
        {% endblock %}


    :copyright: (c) 2010 by the Jinja Team.
    :license: BSD, see LICENSE for more details.
"""
__docformat__ = 'restructuredtext en'
__version__ = '2.8'

# high level interface
from pyse.jinja2.environment import Environment

# loaders
from pyse.jinja2.loaders import FileSystemLoader

__all__ = [
    'Environment', 'FileSystemLoader',
]
