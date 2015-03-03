"""[File Description].

@author       : Nicolas BESSOU <nicolas.bessou@gmail.com>
@copyright    : Copyright 2015, Nicolas BESSOU
"""

__all__ = ['struct']


from namedlist import namedlist
from namedlist import NO_DEFAULT
import pprint

#******************************************************************************
# Local functions
#******************************************************************************
def _isstruct(element):
    return True if hasattr(element, 'structUniqueIdentifier') else False

#******************************************************************************
# Common member functions
#******************************************************************************
def _repr(self):
    """Print as classic dict."""
    return '{{{0}}}'.format(', '.join('\'{0}\': {1!r}'.format(name, getattr(self, name)) for name in self._fields))

def _asdict(self):
    newdict = {}
    for key in self._fields:
        value = getattr(self, key)
        if _isstruct(value):
            newdict[key] = value.asdict()
        else:
            newdict[key] = value
    return newdict
    # return eval(str(self))

def _iteritems(self):
    for key in self._fields:
        yield (key, getattr(self, key))

def _merge(self, container):
    """Merge current struct with another struct or dictionary."""
    if not hasattr(container, 'iteritems'):
        raise TypeError('???')

    for (key, value) in container.iteritems():
        if _isstruct(value) or isinstance(value, dict):
            self.key.merge(value)
        else:
            setattr(self, key, value)


#******************************************************************************
# Factory
#******************************************************************************
def struct(typename, field_names, default=NO_DEFAULT, rename=False,
              use_slots=True):

    nl = namedlist(typename, field_names, default, rename, use_slots)
    nl.__repr__ = _repr
    nl.asdict = _asdict
    nl.iteritems = _iteritems

    nl.structUniqueIdentifier = None
    return nl


#******************************************************************************
# Main
#******************************************************************************
def main():
    Point  = struct('Point', [('x', 0), ('y', 0)])
    Vector = struct('Vector', [('p1', Point()), ('p2', Point())])
    Shape  = struct('Shape', [('v1', Vector()), ('v2', Vector())])

    p1 = Point(2, 3)
    v1 = Vector(Point(), p1)
    s1 = Shape()

    d1 = s1.asdict()

    for (k, v) in s1.iteritems():
        print (k, v)

    # pprint.pprint(d1, width=1)

if __name__ == '__main__':
    main()
