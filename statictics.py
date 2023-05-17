from data import data
from quicksort import quicksort
from sud import search

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
        my_file.write("------ %s; %s шт; %s %s от общей выручки\n" % (
            data[2][i], data[4][i], int(data[6][i] / total * 10000) / 100, "%"))

    my_file.close()