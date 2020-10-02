from memory_profiler import profile
from pympler import asizeof


class Road:
    def __init__(self, length, width):
        self._width = width
        self._length = length

    def mass_count(self, mass, tol):
        print(self._width * self._length * mass * tol)


class Road2:
    __slots__ = ['length', 'width']

    def __init__(self, length, width):
        self.width = width
        self.length = length

    def mass_count(self, mass, tol):
        print(self.width * self.length * mass * tol)


@profile
def testfunc1():
    road_1 = Road(20, 40)


@profile
def testfunc2():
    road_2 = Road2(20, 40)


testfunc1()
testfunc2()

road_3 = Road(20, 40)
road_4 = Road2(20, 40)
print(asizeof.asizeof(road_3))
print(asizeof.asizeof(road_4))