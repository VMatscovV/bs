from data import data
import random


def quicksort(param, fst, lst):
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

    quicksort(param, fst, j)
    quicksort(param, i, lst)