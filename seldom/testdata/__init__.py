import re
import sys
import uuid
import hashlib
import random

from .data import (
    names,
    unicode_names,
    ascii_paragraphs,
    unicode_paragraphs,
    ascii_words,
    unicode_words,
    words,
    first_names_male,
    first_names_female,
    last_names,
)


def get_first_name(gender="", is_unicode=None):
    """
    get first name
    :param gender:
    :param is_unicode:
    :return:
    """
    genders = ["m", "f"]
    if gender:
        gender = str(gender).lower()[0]
        gender = "m" if gender == "1" else "f"
        gender = "m" if gender == "t" else "f"
        if gender not in genders:
            raise ValueError("Unsupported gender, try [m, f, male, female] instead")
    else:
        gender = random.choice(genders)

    if is_unicode is None:
        is_unicode = random.randint(0, 100) < 20

    if is_unicode:
        name = random.choice(unicode_names)
    else:
        if gender == "m":
            name = random.choice(first_names_male)
        else:
            name = random.choice(first_names_female)

    if random.randint(0, 20) == 5:
        name = '{}-{}'.format(name, get_first_name(gender, is_unicode))

    return name.capitalize()


def get_last_name(is_unicode=None):
    """
    get last name
    :param is_unicode:
    :return:
    """
    if is_unicode is None:
        is_unicode = random.randint(0, 100) < 20

    if is_unicode:
        name = random.choice(unicode_names)
    else:
        name = random.choice(last_names)

    if random.randint(0, 20) == 5:
        name = '{}-{}'.format(name, get_last_name(is_unicode))

    return name.capitalize()


def get_username(name=""):
    """
    Returns just a non-space ascii name, this is a very basic username generator
    :param name:
    :return:
    """
    if not name:
        name = get_first_name() if yes() else get_last_name()
    name = re.sub(r"['-]", "", name)
    return name


def get_email(name=''):
    """
    return a random email address
    :param name:
    :return:
    """
    name = get_username(name)
    email_domains = [
        "126.com",
        "163.com",
        "qq.com",
        "sina.com",
        "sohu.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "aol.com",
        "gmail.com",
        "msn.com",
        "comcast.net",
        "hotmail.co.uk",
        "sbcglobal.net",
        "yahoo.co.uk",
        "yahoo.co.in",
        "bellsouth.net",
        "verizon.com",
        "earthlink.net",
        "cox.net",
        "rediffmail.com",
        "yahoo.ca",
        "btinternet.com",
        "charter.net",
        "shaw.ca",
        "ntlworld.com",
        "gmx.com",
        "gmx.net",
        "mail.com",
        "mailinator.com"
    ]

    return '{}@{}'.format(name.lower(), random.choice(email_domains))


def get_md5(val=""):
    """Return an md5 hash of val, if no val then return a random md5 hash

    :param val: string, the value you want to md5 hash
    :returns: string, the md5 hash as a 32 char hex string
    """
    if not val:
        val = get_uuid()

    if getattr(val, "encode", None):
        ret = hashlib.md5(val.encode("utf-8")).hexdigest()
    else:
        ret = hashlib.md5(val).hexdigest()

    return ret


def get_uuid():
    """Generate a random UUID"""
    return str(uuid.uuid4())


def get_float(min_size=None, max_size=None):
    """return a random float

    sames as the random method but automatically sets min and max

    :param min_size: float, the minimum float size you want
    :param max_size: float, the maximum float size you want
    :returns: float, a random value between min_size and max_size
    """
    float_info = sys.float_info
    if min_size is None:
        min_size = float_info.min
    if max_size is None:
        max_size = float_info.max
    return random.uniform(min_size, max_size)


def yes(specifier=0):
    """
    Decide if we should perform this action, this is just a simple way to do something
    I do in tests every now and again

    :Example:
        # EXAMPLE -- simple yes or no question
        if testdata.yes():
            # do this
        else:
            # don't do it

        # EXAMPLE -- multiple choice
        choice = testdata.yes(3)
        if choice == 1:
            # do the first thing
        elif choice == 2:
            # do the second thing
        else:
            # do the third thing

        # EXAMPLE -- do something 75% of the time
        if testdata.yes(0.75):
            # do it the majority of the time
        else:
            # but every once in a while don't do it

    :param specifier: int|float, if int, return a value between 1 and specifier.
        if float, return 1 approximately specifier percent of the time, return 0
        100% - specifier percent of the time
    :returns: integer, usually 1 (True) or 0 (False)
    """
    if specifier:
        if isinstance(specifier, int):
            choice = random.randint(1, specifier)

        else:
            if specifier < 1.0:
                specifier *= 100.0

            specifier = int(specifier)
            x = random.randint(0, 100)
            choice = 1 if x <= specifier else 0

    else:
        choice = random.choice([0, 1])

    return choice
