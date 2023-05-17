import codecs
import random
import datetime


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


def read_csv(filename):
    with codecs.open(filename, "r", "utf_8_sig") as fileObj:
        fileObj.readline()
        for line in fileObj:
            i = 0
            ms = line.strip().split(";")
            if check_input(ms):
                for item in ms:
                    if i == 0 or i > 3:
                        data[i].append(int(item))
                    else:
                        data[i].append(item)
                    i += 1


def total_income(param):
    summ = 0
    for i in data[param]:
        summ += i
    return summ


def maxval(param):
    mx = 0
    for i in range(len(data[param])):
        if data[param][i] > mx:
            mx = data[param][i]
    return mx


def report():

    my_file = open("report.txt", "w+")

    total = total_income(6)
    my_file.write("--- Общая выручка: %s\n" % total)

    my_file.write("\n--- Товар, который продан наибольшее количество раз:\n")
    for i in search(maxval(4), 4):
        my_file.write("------ %s\n" % i[2])

    my_file.write("\n--- Товар, который принёс наибольшую выручку:\n")
    for i in search(maxval(6), 6):
        my_file.write("------ %s\n" % i[2])

    quicksort(6, 0, len(data[6]) - 1)

    my_file.write("\n--- Продано:\n")
    for i in range(len(data[0])):
        my_file.write("------ %s; %s шт; %s %s от общей выручки\n" % (data[2][i], data[4][i], int(data[6][i] / total * 10000) / 100, "%"))

    my_file.close()

def search(el, param):
    result = []
    for i in range(len(data[0])):
        if el == data[param][i]:
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
    return int(arr[6]) == int(arr[4]) * int(arr[5]) or search(arr[0], 0) == [] or check_date(arr[1])


def check_date(date):
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    data = [[], [], [], [], [], [], []]
    read_csv("table.csv")
    report()