import decimal

from wtforms import widgets
from wtforms.fields.core import Field
from wtforms.utils import unset_value

__all__ = (
    "IntegerField",
    "DecimalField",
    "FloatField",
    "IntegerRangeField",
    "DecimalRangeField",
)


class LocaleAwareNumberField(Field):
    """
    Base class for implementing locale-aware number parsing.

    Locale-aware numbers require the 'babel' package to be present.
    """

    def __init__(
        self,
        label=None,
        validators=None,
        use_locale=False,
        number_format=None,
        **kwargs,
    ):
        super().__init__(label, validators, **kwargs)
        self.use_locale = use_locale
        if use_locale:
            self.number_format = number_format
            self.locale = kwargs["_form"].meta.locales[0]
            self._init_babel()





class IntegerField(Field):
    """
    A text field, except all input is coerced to an integer.  Erroneous input
    is ignored and will not be accepted as a value.
    """

    widget = widgets.NumberInput()

    def __init__(self, label=None, validators=None, **kwargs):
        super().__init__(label, validators, **kwargs)





class DecimalField(LocaleAwareNumberField):
    """
    A text field which displays and coerces data of the `decimal.Decimal` type.

    :param places:
        How many decimal places to quantize the value to for display on form.
        If unset, use 2 decimal places.
        If explicitely set to `None`, does not quantize value.
    :param rounding:
        How to round the value during quantize, for example
        `decimal.ROUND_UP`. If unset, uses the rounding value from the
        current thread's context.
    :param use_locale:
        If True, use locale-based number formatting. Locale-based number
        formatting requires the 'babel' package.
    :param number_format:
        Optional number format for locale. If omitted, use the default decimal
        format for the locale.
    """

    widget = widgets.NumberInput(step="any")

    def __init__(
        self, label=None, validators=None, places=unset_value, rounding=None, **kwargs
    ):
        super().__init__(label, validators, **kwargs)
        if self.use_locale and (places is not unset_value or rounding is not None):
            raise TypeError(
                "When using locale-aware numbers, 'places' and 'rounding' are ignored."
            )

        if places is unset_value:
            places = 2
        self.places = places
        self.rounding = rounding




class FloatField(Field):
    """
    A text field, except all input is coerced to an float.  Erroneous input
    is ignored and will not be accepted as a value.
    """

    widget = widgets.TextInput()

    def __init__(self, label=None, validators=None, **kwargs):
        super().__init__(label, validators, **kwargs)




class IntegerRangeField(IntegerField):
    """
    Represents an ``<input type="range">``.
    """

    widget = widgets.RangeInput()


class DecimalRangeField(DecimalField):
    """
    Represents an ``<input type="range">``.
    """

    widget = widgets.RangeInput(step="any")
