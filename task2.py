import random

ra = [i for i in random.sample(range(0, 50), len(range(0, 50)))]
print(ra)


def merge_sort(rnd_list, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(rnd_list, start, mid)
        merge_sort(rnd_list, mid, end)
        merge_list(rnd_list, start, mid, end)


def merge_list(rnd_list, start, mid, end):
    left = rnd_list[start:mid]
    right = rnd_list[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            rnd_list[k] = left[i]
            i = i + 1
        else:
            rnd_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            rnd_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            rnd_list[k] = right[j]
            j = j + 1
            k = k + 1


merge_sort(ra, 0, len(ra))
print(ra)
