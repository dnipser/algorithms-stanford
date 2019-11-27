
def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def copy(array):
    res = []
    for i in array:
        res.append(i)
    return res


def is_sorted(array):
    sorted = True
    i = 0
    for j in range(1, len(array)):
        if array[i] > array[j]:
            sorted = False
            break
        i += 1
    return sorted
