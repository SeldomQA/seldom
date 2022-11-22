from shlex import quote


def to_curl(request, compressed: bool = False, verify: bool = True) -> str:
    """
    Returns string with curl command by provided request object
    :param request: request object
    :param compressed:
        If `True` then `--compressed` argument will be added to result
    :param verify:
    """
    parts = [
        ('curl', None),
        ('-X', request.method),
    ]

    for key, value in sorted(request.headers.items()):
        parts += [('-H', f'{key}: {value}')]

    if request.body:
        body = request.body
        if isinstance(body, bytes):
            body = body.decode('utf-8')
        parts += [('-d', body)]

    if compressed:
        parts += [('--compressed', None)]

    if not verify:
        parts += [('--insecure', None)]

    parts += [(None, request.url)]

    flat_parts = []
    for key, value in parts:
        if key:
            flat_parts.append(quote(key))
        if value:
            flat_parts.append(quote(value))

    return ' '.join(flat_parts)
