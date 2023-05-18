def binary_search(arr, elem):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high)//2
        if arr[middle] == elem:
            return middle
        elif arr[middle] < elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1