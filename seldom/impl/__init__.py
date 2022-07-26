from seldom.running.config import Seldom
from seldom.impl.html import get_easily_readable_snippet
from collections import namedtuple, OrderedDict
from copy import copy


class GUIElement:
    def __init__(self):
        self._driver = Seldom.driver
        self._args = []
        self._kwargs = OrderedDict()
        self._impl_cached = None

    def exists(self):
        """
        Evaluates to true if this GUI element exists.
        """
        return self._impl.exists()

    def with_impl(self, impl):
        result = copy(self)
        result._impl = impl
        return result

    @property
    def _impl(self):
        if self._impl_cached is None:
            impl_class = \
                getattr(helium._impl, self.__class__.__name__ + 'Impl')
            self._impl_cached = impl_class(
                self._driver, *self._args, **self._kwargs
            )
        return self._impl_cached

    @_impl.setter
    def _impl(self, value):
        self._impl_cached = value

    def __repr__(self):
        return self._repr_constructor_args(self._args, self._kwargs)

    def _repr_constructor_args(self, args=None, kwargs=None):
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        return '%s(%s)' % (
            self.__class__.__name__,
            repr_args(self.__init__, args, kwargs, repr)
        )

    def _is_bound(self):
        return self._impl_cached is not None and self._impl_cached._is_bound()


class HTMLElement(GUIElement):
    def __init__(
            self, below=None, to_right_of=None, above=None, to_left_of=None
    ):
        super(HTMLElement, self).__init__()
        self._kwargs['below'] = below
        self._kwargs['to_right_of'] = to_right_of
        self._kwargs['above'] = above
        self._kwargs['to_left_of'] = to_left_of

    @property
    def width(self):
        """
        The width of this HTML element, in pixels.
        """
        return self._impl.width

    @property
    def height(self):
        """
        The height of this HTML element, in pixels.
        """
        return self._impl.height

    @property
    def x(self):
        """
        The x-coordinate on the page of the top-left point of this HTML element.
        """
        return self._impl.x

    @property
    def y(self):
        """
        The y-coordinate on the page of the top-left point of this HTML element.
        """
        return self._impl.y

    @property
    def top_left(self):
        """
        The top left corner of this element, as a :py:class:`helium.Point`.
        This point has exactly the coordinates given by this element's `.x` and
        `.y` properties. `top_left` is for instance useful for clicking at an
        offset of an element::

            click(Button("OK").top_left + (30, 15))
        """
        return self._impl.top_left

    @property
    def web_element(self):
        """
        The Selenium WebElement corresponding to this element.
        """
        return self._impl.web_element

    def __repr__(self):
        if self._is_bound():
            element_html = self.web_element.get_attribute('outerHTML')
            return get_easily_readable_snippet(element_html)
        else:
            return super(HTMLElement, self).__repr__()


class Text(HTMLElement):
    """
    Lets you identify any text or label on a web page. This is most useful for
    checking whether a particular text exists::

        if Text("Do you want to proceed?").exists():
            click("Yes")

    ``Text`` also makes it possible to read plain text data from a web page. For
    example, suppose you have a table of people's email addresses. Then you
    can read John's email addresses as follows::

        Text(below="Email", to_right_of="John").value

    Similarly to ``below`` and ``to_right_of``, the keyword parameters ``above``
    and ``to_left_of`` can be used to search for texts above and to the left of
    other web elements.
    """

    def __init__(
            self, text=None, below=None, to_right_of=None, above=None,
            to_left_of=None
    ):
        super(Text, self).__init__(
            below=below, to_right_of=to_right_of, above=above,
            to_left_of=to_left_of
        )
        self._args.append(text)

    @property
    def value(self):
        """
        Returns the current value of this Text object.
        """
        return self._impl.value
