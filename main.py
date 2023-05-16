import codecs
import random
import datetime


def quicksort(param, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    q = data[param][random.randint(fst, lst)]

    while i <= j:
        while data[param][i] < q:
            i += 1
        while data[param][j] > q:
            j -= 1
        if i <= j:
            for l in range(7):
                data[l][i], data[l][j] = data[l][j], data[l][i]
            i, j = i + 1, j - 1

    quicksort(param, fst, j)
    quicksort(param, i, lst)


def read_csv(filename):
    bd = [[], [], [], [], [], [], []]
    with codecs.open(filename, "r", "utf_8_sig") as fileObj:
        fileObj.readline()
        for line in fileObj:
            i = 0
            ms = line.strip().split(";")
            if check_input(ms):
                for item in ms:
                    if i == 0 or i > 3:
                        bd[i].append(int(item))
                    else:
                        bd[i].append(item)
                    i += 1
    return bd


def total_income(arr):
    summ = 0
    for i in arr:
        summ += i
    return summ


def indexmaxval(arr):
    mx = 0
    ind = 0
    for i in range(len(arr)):
        if arr[i] > mx:
            mx = arr[i]
            ind = i
    return ind


def report():
    total = total_income(data[6])
    print("--- Общая выручка:", total)
    print("--- Продано:")
    for i in range(len(data[0])):
        print("------", data[2][i], ";", data[4][i], "шт;", int(data[6][i] / total * 10000) / 100, "% от общей выручки")


def search(el):
    result = []
    for i in range(len(data[0])):
        if el == data[0][i] or el == data[1][i] or el == data[2][i] or el == data[3][i]:
            obj = []
            for j in range(7):
                obj.append(data[j][i])
            result.append(obj)
    return result


def delete(el):
    for i in range(len(data[0])):
        if el == data[0][i]:
            for j in range(7):
                data[j].pop(i)
            break

def check_input(arr):
        return int(arr[6]) == int(arr[4])*int(arr[5]) or search(arr[0]) == [] or check_date(arr[1])

def check_date(date):
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


data = [[]]
data = read_csv("table.csv")

print(data)

print(total_income(data[6]))

print(data[2][indexmaxval(data[4])])

print(data[2][indexmaxval(data[6])])

report()

print(data)

print(search('04.11.2022'))

delete(5004)

print(search('04.11.2022'))

quicksort(6, 0, len(data[6]) - 1)

print(data)
