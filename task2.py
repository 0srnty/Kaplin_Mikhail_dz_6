from dataclasses import make_dataclass
from memory_profiler import profile
from pympler import asizeof


class Road:
    def __init__(self, length, width):
        self._width = width
        self._length = length


Road2 = make_dataclass('Road2', ('length', 'width'))

road_3 = Road(20, 40)
road_4 = Road2(20, 40)
print(asizeof.asizeof(road_3))
print(asizeof.asizeof(road_4))
