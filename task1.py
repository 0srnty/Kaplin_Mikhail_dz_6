import random

ra = [i for i in random.sample(range(-100, 100), len(range(-100, 100)))]
print(ra)


def sort1(rnd_list):
    n = 1
    while n < len(rnd_list):
        for i in range(len(rnd_list) - n):
            if rnd_list[i] < rnd_list[i + 1]:
                rnd_list[i], rnd_list[i + 1] = rnd_list[i + 1], rnd_list[i]
        n += 1
    return rnd_list


print(sort1(ra))
