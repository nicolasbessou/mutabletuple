"""[File Description].

@author       : Nicolas BESSOU <nicolas.bessou@gmail.com>
@copyright    : Copyright 2015, Nicolas BESSOU
"""

__all__ = ['mutabletuple']


from namedlist import namedlist, NO_DEFAULT

#******************************************************************************
# Local functions
#******************************************************************************
def _ismutabletuple(element):
    return True if hasattr(element, 'mutabletupleUniqueIdentifier') else False

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
        if _ismutabletuple(value):
            newdict[key] = value.asdict()
        else:
            newdict[key] = value
    return newdict
    # return eval(str(self))

def _iteritems(self):
    for key in self._fields:
        yield (key, getattr(self, key))

def _merge(self, container):
    """Merge current mutabletuple with another mutabletuple or dictionary."""
    if not hasattr(container, 'iteritems'):
        raise TypeError('???')

    for (key, value) in container.iteritems():
        if _ismutabletuple(value) or isinstance(value, dict):
            self.key.merge(value)
        else:
            setattr(self, key, value)


#******************************************************************************
# Factory
#******************************************************************************
def mutabletuple(typename, field_names, default=NO_DEFAULT, rename=False,
              use_slots=True):

    nl = namedlist(typename, field_names, default, rename, use_slots)
    nl.__repr__ = _repr
    nl.asdict = _asdict
    nl.iteritems = _iteritems

    nl.mutabletupleUniqueIdentifier = None
    return nl


#******************************************************************************
# Main
#******************************************************************************
def main():
    Point  = mutabletuple('Point', [('x', 0), ('y', 0)])
    Vector = mutabletuple('Vector', [('p1', Point()), ('p2', Point())])
    Shape  = mutabletuple('Shape', [('v1', Vector()), ('v2', Vector())])

    p1 = Point(2, 3)
    v1 = Vector(Point(), p1)
    s1 = Shape()

    d1 = s1.asdict()

    for (k, v) in s1.iteritems():
        print (k, v)

    # pprint.pprint(d1, width=1)

if __name__ == '__main__':
    main()
