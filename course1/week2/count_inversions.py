
import time
from misc.file_utils import read_input_dataset


def calculate_inversions(left_tuple, right_tuple):
    left_array = left_tuple[0]
    right_array = right_tuple[0]
    sorted_array = []
    inversions = left_tuple[1] + right_tuple[1]

    li = ri = 0
    # copy values from left and right sub arrays in ascending order
    while li < len(left_array) and ri < len(right_array):
        if left_array[li] <= right_array[ri]:
            sorted_array.append(left_array[li])
            li += 1
        else:
            sorted_array.append(right_array[ri])
            ri += 1

            # increment number of inversions by number of elements remaining
            # in left sub array. That goes from the fact that su arrays are
            # sorted, so all elements remaining of left sub array are bigger
            # than element copied from the right sub array and they will be
            # swapped by next iterations
            inversions += len(left_array) - li

    # copy remaining parts which might left
    # in case if sub arrays have different size
    while li < len(left_array):
        sorted_array.append(left_array[li])
        li += 1

    while ri < len(right_array):
        sorted_array.append(right_array[ri])
        ri += 1

    return (sorted_array, inversions)


def sort_with_inversions(input_tuple):
    array = input_tuple[0]
    if len(array) == 1:
        return input_tuple

    half_length = len(array) // 2
    left_unsorted = array[:half_length]
    right_unsorted = array[half_length:]

    left_tuple = sort_with_inversions((left_unsorted, 0))
    right_tuple = sort_with_inversions((right_unsorted, 0))

    sorted_tuple = calculate_inversions(left_tuple, right_tuple)
    return sorted_tuple


if __name__ == '__main__':
    # given_arr = [1, 3, 5, 2, 4, 6]
    # given_arr = [1, 3, 0, 12, 11, 9, 14, 10, 15, 4, 13, 8, 5, 6, 2, 7]
    given_arr = read_input_dataset(
        '/mnt/c/work/projects/algorithms-stanford/course1/week2/',
        'IntegerArray.txt')

    print("Given array: ", given_arr)

    given_tuple = (given_arr, 0)

    start = time.time()
    sorted_tuple = sort_with_inversions(given_tuple)
    end = time.time()
    print("Sorted array: ", sorted_tuple[0])
    print("Number of inversions: {}, elapsed time: {}".format(
            sorted_tuple[1], end - start))
