"""Test package."""

# Package to test
from mutabletuple import mutabletuple

# Native import
import sys
import unittest
import pickle
from collections import OrderedDict

__all__ = ['TestMutableTuple']

# def main():
#     Point  = mutabletuple('Point', [('x', 0), ('y', 0)])
#     Vector = mutabletuple('Vector', [('p1', Point()), ('p2', Point())])
#     Shape  = mutabletuple('Shape', [('v1', Vector()), ('v2', Vector())])

#     p1 = Point(2, 3)
#     v1 = Vector(Point(), p1)
#     s1 = Shape()

#     d1 = s1._asdict()

#     for (k, v) in s1.iteritems():
#         print (k, v)

#     # pprint.pprint(d1, width=1)


class TestMutableTuple(unittest.TestCase):
    def test_simple(self):
        # Declare members as string
        Point = mutabletuple('Point', 'x y')
        p = Point(10, 20)
        self.assertEqual(str(p), "{'x': 10, 'y': 20}")

        # Declare members as list
        Point = mutabletuple('Point', ['x', 'y'])
        p = Point(10, 20)
        self.assertEqual(str(p), "{'x': 10, 'y': 20}")

        # Declare members as list with default
        Point = mutabletuple('Point', [('x', 10), ('y', 20)])
        p = Point()
        self.assertEqual(str(p), "{'x': 10, 'y': 20}")

        self.assertEqual(Point(10, 11), Point(10, 11))
        self.assertNotEqual(Point(10, 11), Point(10, 12))

    def test_dict(self):
        Point = mutabletuple('Point', ['x', 'y'])
        p = Point(10, 20)
        self.assertEqual(p._asdict(), {'x': 10, 'y': 20})

    def test_default(self):
        Point = mutabletuple('Point', 'x y z', default=100)
        self.assertEqual(Point(), Point(100, 100, 100))
        self.assertEqual(Point(10), Point(10, 100, 100))
        self.assertEqual(Point(10, 20), Point(10, 20, 100))
        self.assertEqual(Point(10, 20, 30), Point(10, 20, 30))
        self.assertEqual(Point()._asdict(), {'x': 100, 'y': 100, 'z': 100})


    # Test add key
    # Test remove key
    # Test nested
    # Test JSON
    # Test from dict
    # Test getattr, setattr

    def test_writable(self):
        Point = mutabletuple('Point', ['x', ('y', 10), ('z', 20)], 100)
        p = Point(0)
        self.assertEqual((p.x, p.y, p.z), (0, 10, 20))
        p.x = -1
        self.assertEqual((p.x, p.y, p.z), (-1, 10, 20))
        p.y = -1
        self.assertEqual((p.x, p.y, p.z), (-1, -1, 20))
        p.z = None
        self.assertEqual((p.x, p.y, p.z), (-1, -1, None))


    def test_iteration(self):
        Point = mutabletuple('Point', ['x', ('y', 10), ('z', 20)], [1, 2, 3])
        p = Point()
        self.assertEqual(len(p), 3)

        self.assertEqual(list(iter(p)), [[1, 2, 3], 10, 20])

        for expected, found in zip([[1, 2, 3], 10, 20], p):
            self.assertEqual(expected, found)

        for expected, found in zip((('x', [1, 2, 3]), ('y', 10), ('z', 20)), p.iteritems()):
            self.assertEqual(expected, found)


    def test_getitem(self):
        Point = mutabletuple('Point', 'a b')
        p = Point(1, 2)
        self.assertEqual((p[0], p[1]), (1, 2))
        self.assertEqual(list(p), [1, 2])
        self.assertRaises(IndexError, p.__getitem__, 2)

    def test_setitem(self):
        Point = mutabletuple('Point', 'a b')
        p = Point(1, 2)
        p[0] = 10
        self.assertEqual(list(p), [10, 2])
        p[1] = 20
        self.assertEqual(list(p), [10, 20])
        self.assertRaises(IndexError, p.__setitem__, 2, 3)


# *****************************************************************************
# Pickle test
# *****************************************************************************
# test both pickle and cPickle in 2.x, but just pickle in 3.x
try:
    import cPickle
    pickle_modules = (pickle, cPickle)
except ImportError:
    pickle_modules = (pickle,)

# types used for pickle tests
TestMT0 = mutabletuple('TestMT0', '')
TestMT = mutabletuple('TestMT', 'x y z')

# class TestMutableTuplePickle(unittest.TestCase):
    # def test_pickle(self):
    #     for p in (TestMT0(), TestMT(x=10, y=20, z=30)):
    #         for module in pickle_modules:
    #             for protocol in range(-1, module.HIGHEST_PROTOCOL + 1):
    #                 q = module.loads(module.dumps(p, protocol))
    #                 self.assertEqual(p, q)
    #                 self.assertEqual(p._fields, q._fields)
    #                 self.assertNotIn(b'OrderedDict', module.dumps(p, protocol))

