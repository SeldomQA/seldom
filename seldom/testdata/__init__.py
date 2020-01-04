import re
import sys
import uuid
import random
import hashlib
import datetime

from .data import (
    unicode_names,
    words_str,
    first_names_male,
    first_names_female,
    last_names,
)


def first_name(gender="", is_unicode=None):
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
        name = '{}-{}'.format(name, first_name(gender, is_unicode))

    return name.capitalize()


def last_name(is_unicode=None):
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
        name = '{}-{}'.format(name, last_name(is_unicode))

    return name.capitalize()


def username(name=""):
    """
    Returns just a non-space ascii name, this is a very basic username generator
    """
    if not name:
        name = first_name() if yes() else last_name()
    name = re.sub(r"['-]", "", name)
    return name


def get_email(name=''):
    """
    return a random email address
    """
    name = username(name)
    email_domains = [
        "126.com",
        "163.com",
        "qq.com",
        "sina.com",
        "sohu.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "gmail.com",
        "msn.com",
        "mail.com",
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
    """
    Generate a random UUID
    """
    return str(uuid.uuid4())


def get_int(min_size=1, max_size=sys.maxsize):
    """
    return integer style data
    :param min_size:
    :param max_size:
    """
    return random.randint(min_size, max_size)


def get_int32(min_size=1):
    """returns a 32-bit positive integer"""
    return random.randint(min_size, 2**31-1)


def get_int64(min_size=1):
    """returns up to a 64-bit positive integer"""
    return random.randint(min_size, 2**63-1)


def get_float(min_size=None, max_size=None):
    """
    return a random float
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


def get_digits(count):
    """
    return a string value that contains count digits
    :param count: int, how many digits you want, so if you pass in 4, you would get
        4 digits
    :returns: string, this returns a string because the digits might start with
        zero
    """
    max_size = int("9" * count)
    ret = "{{:0>{}}}".format(count).format(get_int(0, max_size))
    return ret


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


def get_words(count=0, as_str=True, words=None):
    """get some amount of random words
    :param count: integer, how many words you want, 0 means a random amount (at most 20)
    :param as_str: boolean, True to return as string, false to return as list of words
    :param words: list, a list of words to choose from, defaults to unicode + ascii words
    :returns: unicode|list, your requested words
    """
    # since we specified we didn't care, randomly choose how many words there should be
    if count == 0:
        count = random.randint(1, 20)

    if not words:
        words = words_str

    ret_words = random.sample(words, count)
    return ret_words if not as_str else ' '.join(ret_words)


def get_word(words=None):
    return get_words(1, as_str=True, words=words)


def get_birthday(as_str=False, start_age=18, stop_age=100):
    """
    return a random YYYY-MM-DD
    :param as_str: boolean, true to return the bday as a YYYY-MM-DD string
    :param start_age: int, minimum age of the birthday date
    :param stop_age: int, maximum age of the birthday date
    :returns: datetime.date|string
    """
    age = random.randint(start_age, stop_age)
    year = (datetime.datetime.utcnow() - datetime.timedelta(weeks=(age * 52))).year
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
    elif month in [9, 4, 6, 11]:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    birthday = datetime.date(year, month, day)
    if as_str:
        birthday = "{:%Y-%m-%d}".format(birthday)

    return birthday


def get_past_datetime(now=None):
    """
    return a datetime guaranteed to be in the past from now
    """
    if not now:
        now = datetime.datetime.now()
    if isinstance(now, datetime.timedelta):
        now = datetime.datetime.now() - now

    td = now - datetime.datetime(year=2000, month=1, day=1)
    return now - datetime.timedelta(
        days=random.randint(1, max(td.days, 1)),
        seconds=random.randint(1, max(td.seconds, 1))
    )


def get_future_datetime(now=None):
    """
    return a datetime guaranteed to be in the future from now
    """
    if not now:
        now = datetime.datetime.now()
    if isinstance(now, datetime.timedelta):
        now = datetime.datetime.now() + now

    return now + datetime.timedelta(
        weeks=random.randint(1, 52 * 50),
        hours=random.randint(0, 24),
        days=random.randint(0, 365),
        seconds=random.randint(0, 86400)
    )


def get_now_time():
    """
    Get date, default to current day。
    :return:
    """
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return date


def get_date(day=None):
    """
    Get date, default to current day。
    :return:
    """
    if day is None:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
    else:
        date = (datetime.datetime.now() + datetime.timedelta(days=day)).strftime("%Y-%m-%d")

    return date
