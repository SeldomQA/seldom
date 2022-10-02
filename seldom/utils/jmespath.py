"""
jmespath search data
https://github.com/jmespath/jmespath.py
"""
from jmespath import search


def jmespath(data, expression, options=None):
    """
    search jmespath data
    """
    return search(expression, data, options)
