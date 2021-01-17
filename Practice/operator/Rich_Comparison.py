import operator as op


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


'''
    def __eq__(self, other):
        if not isinstance(other, point):
            return False
        try:
            return self.x == other.x and self.y == other.y
        except AttributeError:
            return False
'''


point_1 = point(3, 3)
point_2 = point(2, 2)
point_3 = point(3, 3)
A = 6


'''
print(op.eq(point_1, point_2))
print(op.eq(point_1, point_3))
print(op.eq(point_1, None))
print()
print(point_1 == point_2)
print(point_1 == point_3)
print(point_1 == None)
'''


print(point_1 == 6)
print(point_1.__eq__(6))
