from wtforms.utils import unset_value

from .. import widgets
from .core import Field

__all__ = ("FormField",)


class FormField(Field):
    """
    Encapsulate a form as a field in another form.

    :param form_class:
        A subclass of Form that will be encapsulated.
    :param separator:
        A string which will be suffixed to this field's name to create the
        prefix to enclosed fields. The default is fine for most uses.
    """

    widget = widgets.TableWidget()

    def __init__(
        self, form_class, label=None, validators=None, separator="-", **kwargs
    ):
        super().__init__(label, validators, **kwargs)
        self.form_class = form_class
        self.separator = separator
        self._obj = None
        if self.filters:
            raise TypeError(
                "FormField cannot take filters, as the encapsulated"
                " data is not mutable."
            )
        if validators:
            raise TypeError(
                "FormField does not accept any validators. Instead,"
                " define them on the enclosed form."
            )




    def __iter__(self):
        return iter(self.form)

    def __getitem__(self, name):
        return self.form[name]

    def __getattr__(self, name):
        return getattr(self.form, name)


