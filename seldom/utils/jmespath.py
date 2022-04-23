from jmespath import search


def jmespath(data, expression, options=None):
    """
    jmespath search data
    https://github.com/jmespath/jmespath.py
    """
    return search(expression, data, options)
