from data import data
import codecs
import  datetime

def check_sum(arr):
    return int(arr[6]) == int(arr[4]) * int(arr[5])


def check_id(id):
    return search(id, 0) == []


def check_date(date):
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except:
        return False

def read_csv(filename):
    with codecs.open(filename, "r", "utf_8_sig") as fileObj:
        fileObj.readline()
        for line in fileObj:
            new_input(line.strip().split(";"))


def new_input(ms):
    i = 0

    if not check_sum(ms):
        ms[6] = int(ms[4]) * int(ms[5])

    if not check_date(ms[1]):
        ms[1] = "--.--.----"

    if not check_id(ms[0]):
        ms[0] = "88005553535%s" % i

    for item in ms:
        if i == 0 or i > 3:
            data[i].append(int(item))
        else:
            data[i].append(item)
        i += 1

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
