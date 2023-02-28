from collections import namedtuple


def my_foo():
    pass


if __name__ == '__main__':
    Point = namedtuple('Point', ['x', 'y'])
    point = Point(3, 7)
    print(point)
    print(point.x, point.y)
    print(type(point))
    print(type(namedtuple('Point', ['x', 'y'])))