from data import data
import random


def quicksort(nums, fst, lst):
    if fst >= lst: return nums

    i, j = fst, lst
    q = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] > q: i += 1
        while nums[j] < q: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    quicksort(nums, fst, j)
    quicksort(nums, i, lst)
    return nums

def quicksort_data(param, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    q = data[param][random.randint(fst, lst)]

    while i <= j:
        while data[param][i] > q:
            i += 1
        while data[param][j] < q:
            j -= 1
        if i <= j:
            for l in range(7):
                data[l][i], data[l][j] = data[l][j], data[l][i]
            i, j = i + 1, j - 1

    quicksort_data(param, fst, j)
    quicksort_data(param, i, lst)