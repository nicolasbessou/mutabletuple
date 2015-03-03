"""[File Description].

@author       : Nicolas BESSOU <nicolas.bessou@gmail.com>
@copyright    : Copyright 2015, Nicolas BESSOU
"""

from namedlist import namedlist, NO_DEFAULT

__all__ = ['mutabletuple']


# *****************************************************************************
# Local functions
# *****************************************************************************
def _ismutabletuple(element):
    return True if hasattr(element, 'MutableTupleUniqueIdentifier') else False


# *****************************************************************************
# Common member functions that extends namedlist functionality
# *****************************************************************************
def _mt_repr(self):
    """Print like dict."""
    return '{{{0}}}'.format(', '.join('\'{0}\': {1!r}'.format(name, getattr(self, name)) for name in self._fields))


def _mt_asdict(self):
    """Recursively convert mutabletuple to a dict."""
    newdict = {}
    for key in self._fields:
        value = getattr(self, key)
        if _ismutabletuple(value):
            newdict[key] = value.asdict()
        else:
            newdict[key] = value
    return newdict


def _mt_iteritems(self):
    """Iterate like dict."""
    for key in self._fields:
        yield (key, getattr(self, key))


def _mt_merge(self, container):
    """Merge current mutabletuple with another mutabletuple or dictionary."""
    if not hasattr(container, 'iteritems'):
        raise TypeError('???')

    for (key, value) in container.iteritems():
        if _ismutabletuple(value) or isinstance(value, dict):
            self.key.merge(value)
        else:
            setattr(self, key, value)


def _mt_getattr(self, attr):
    """Get attribute from []."""
    return self[attr]


def _mt_setattr(self, attr, value):
    """Set attribute from []."""
    self[attr] = value


# *****************************************************************************
# Factory
# *****************************************************************************
def mutabletuple(typename, field_names, default=NO_DEFAULT):
    """Factory function that creates a mutabletuple."""
    newtuple = namedlist(typename, field_names, default)

    # Declare unique identifier to identify namedtuple class
    newtuple.MutableTupleUniqueIdentifier = None

    # Extend namedlist functionality
    newtuple.__repr__  = _mt_repr
    newtuple._asdict   = _mt_asdict
    newtuple.iteritems = _mt_iteritems

    return newtuple
