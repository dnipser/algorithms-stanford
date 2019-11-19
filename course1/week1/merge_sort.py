

def merge(left_array, right_array):
    sorted_array = []

    li = ri = 0
    # copy values from left and right sub arrays in ascending order
    while li < len(left_array) and ri < len(right_array):
        if left_array[li] <= right_array[ri]:
            sorted_array.append(left_array[li])
            li += 1
        else:
            sorted_array.append(right_array[ri])
            ri += 1

    # copy remaining parts which might left
    # in case if sub arrays have different size
    while li < len(left_array):
        sorted_array.append(left_array[li])
        li += 1

    while ri < len(right_array):
        sorted_array.append(right_array[ri])
        ri += 1

    return sorted_array


def merge_sort(array):
    if len(array) == 1:
        return array

    half_length = len(array) // 2
    left_unsorted = array[:half_length]
    right_unsorted = array[half_length:]

    left_sorted = merge_sort(left_unsorted)
    right_sorted = merge_sort(right_unsorted)

    sorted_array = merge(left_sorted, right_sorted)
    return sorted_array


if __name__ == '__main__':
    given_arr = [1, 3, 0, 12, 11, 9, 14, 10, 15, 4, 13, 8, 5, 6, 2, 7]
    print("Given array: ", given_arr)
    sorted_arr = merge_sort(given_arr)
    print("Sorted array: ", sorted_arr)
