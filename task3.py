import random
from statistics import median

m = int(input())
l = 2 * m + 1
ra = [i for i in random.sample(range(50), len(range(l)))]
print(ra)


def sort2(rnd_list):
    rnd_list = sorted(rnd_list)
    if len(rnd_list) % 2 == 1:
        return rnd_list[int(len(rnd_list) / 2)]
    else:
        return 0.5 * (rnd_list[len(rnd_list) / 2 - 1] + rnd_list[len(rnd_list) / 2])


print(sort2(ra))
print(median(ra))