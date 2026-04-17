import itertools

from wtforms.utils import unset_value

from .. import widgets
from .core import Field
from .core import UnboundField

__all__ = ("FieldList",)


class FieldList(Field):
    """
    Encapsulate an ordered list of multiple instances of the same field type,
    keeping data as a list.

    >>> authors = FieldList(StringField('Name', [validators.DataRequired()]))

    :param unbound_field:
        A partially-instantiated field definition, just like that would be
        defined on a form directly.
    :param min_entries:
        if provided, always have at least this many entries on the field,
        creating blank ones if the provided input does not specify a sufficient
        amount.
    :param max_entries:
        accept no more than this many entries as input, even if more exist in
        formdata.
    :param separator:
        A string which will be suffixed to this field's name to create the
        prefix to enclosed list entries. The default is fine for most uses.
    """

    widget = widgets.ListWidget()

    def __init__(
        self,
        unbound_field,
        label=None,
        validators=None,
        min_entries=0,
        max_entries=None,
        separator="-",
        default=(),
        **kwargs,
    ):
        super().__init__(label, validators, default=default, **kwargs)
        if self.filters:
            raise TypeError(
                "FieldList does not accept any filters. Instead, define"
                " them on the enclosed field."
            )
        assert isinstance(
            unbound_field, UnboundField
        ), "Field must be unbound, not a field class"
        self.unbound_field = unbound_field
        self.min_entries = min_entries
        self.max_entries = max_entries
        self.last_index = -1
        self._prefix = kwargs.get("_prefix", "")
        self._separator = separator
        self._field_separator = unbound_field.kwargs.get("separator", "-")


    def _extract_indices(self, prefix, formdata):
        """
        Yield indices of any keys with given prefix.

        formdata must be an object which will produce keys when iterated.  For
        example, if field 'foo' contains keys 'foo-0-bar', 'foo-1-baz', then
        the numbers 0 and 1 will be yielded, but not necessarily in order.
        """
        pass

    def validate(self, form, extra_validators=()):
        """
        Validate this FieldList.

        Note that FieldList validation differs from normal field validation in
        that FieldList validates all its enclosed fields first before running any
        of its own validators.
        """
        pass



    def append_entry(self, data=unset_value):
        """
        Create a new entry with optional default data.

        Entries added in this way will *not* receive formdata however, and can
        only receive object data.
        """
        pass

    def pop_entry(self):
        """Removes the last entry from the list and returns it."""
        pass

    def __iter__(self):
        return iter(self.entries)

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, index):
        return self.entries[index]

