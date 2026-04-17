import os


def messages_path():
    """
    Determine the path to the 'messages' directory as best possible.
    """
    pass


def get_builtin_gnu_translations(languages=None):
    """
    Get a gettext.GNUTranslations object pointing at the
    included translation files.

    :param languages:
        A list of languages to try, in order. If omitted or None, then
        gettext will try to use locale information from the environment.
    """
    pass


def get_translations(languages=None, getter=get_builtin_gnu_translations):
    """
    Get a WTForms translation object which wraps a low-level translations object.

    :param languages:
        A sequence of languages to try, in order.
    :param getter:
        A single-argument callable which returns a low-level translations object.
    """
    return getter(languages)


class DefaultTranslations:
    """
    A WTForms translations object to wrap translations objects which use
    ugettext/ungettext.
    """

    def __init__(self, translations):
        self.translations = translations




class DummyTranslations:
    """
    A translations object which simply returns unmodified strings.

    This is typically used when translations are disabled or if no valid
    translations provider can be found.
    """


