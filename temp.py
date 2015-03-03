from namedlist import namedlist

Point = namedlist('Point', ['x', 'y'])
p1 = Point(0, 0)

print p1
print list(iter(p1))
