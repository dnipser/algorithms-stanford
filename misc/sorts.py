
def bubble_sort(array):
    """
    https://en.wikipedia.org/wiki/Bubble_sort#/media/File:Bubble-sort-example-300px.gif
    https://en.wikipedia.org/wiki/Bubble_sort
    https://www.toptal.com/developers/sorting-algorithms/bubble-sort
    """
    iterations_count = 0
    while True:
        swapped = False
        for i in range((len(array) - 1) - iterations_count):
            if array[i] > array[i + 1]:
                __swap(array, i, i + 1)
                swapped = True
        if swapped is False:
            break

        iterations_count += 1
    return array


def insertion_sort(array):
    """
    https://en.wikipedia.org/wiki/Insertion_sort
    https://www.toptal.com/developers/sorting-algorithms/insertion-sort
    https://www.geeksforgeeks.org/insertion-sort/
    """
    for i in range(1, len(array)):
        outer_val = array[i]
        j = i - 1
        while j >= 0 and array[j] > outer_val:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = outer_val
    return array


def selection_sort(array):
    """
    https://en.wikipedia.org/wiki/Selection_sort#/media/File:Selection-Sort-Animation.gif
    https://en.wikipedia.org/wiki/Selection_sort
    https://www.toptal.com/developers/sorting-algorithms/selection-sort
    """
    for i in range(len(array)):
        val_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[val_index]:
                val_index = j

        if val_index != i:
            __swap(array, i, val_index)
    return array


def merge_sort(array):
    """
    https://www.geeksforgeeks.org/merge-sort/
    https://en.wikipedia.org/wiki/Merge_sort
    https://www.toptal.com/developers/sorting-algorithms/merge-sort
    """
    if len(array) == 1:
        return array

    half_length = len(array) // 2
    left_unsorted = array[:half_length]
    right_unsorted = array[half_length:]

    left_sorted = merge_sort(left_unsorted)
    right_sorted = merge_sort(right_unsorted)

    sorted_array = __ms_merge(left_sorted, right_sorted)
    return sorted_array


def __ms_merge(left_array, right_array):
    sorted_array = []

    li = ri = 0
    while li < len(left_array) and ri < len(right_array):
        if left_array[li] <= right_array[ri]:
            sorted_array.append(left_array[li])
            li += 1
        else:
            sorted_array.append(right_array[ri])
            ri += 1

    while li < len(left_array):
        sorted_array.append(left_array[li])
        li += 1

    while ri < len(right_array):
        sorted_array.append(right_array[ri])
        ri += 1

    return sorted_array


def quick_sort(array, lo=0, hi=-1):
    """
    https://www.geeksforgeeks.org/quick-sort/
    https://en.wikipedia.org/wiki/Quicksort
    https://www.toptal.com/developers/sorting-algorithms/quick-sort
    """

    if hi < 0:
        hi = len(array) - 1

    if lo < hi:
        partition_idx = __qs_partition_middle(array, lo, hi)
        quick_sort(array, lo, partition_idx - 1)
        quick_sort(array, partition_idx + 1, hi)
    return array


def __qs_partition_middle(array, lo, hi):
    # select medium array element as a pivot, then iterate from
    # beginning and end of array towards to middle and swap elements
    # so smaller are right to pivot and bigger are right to pivot
    pivot_idx = lo + (hi - lo) // 2
    pivot = array[pivot_idx]

    i = lo
    j = hi
    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            break

        __swap(array, i, j)

    return i


def __swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def __copy(input):
    res = []
    for i in input:
        res.append(i)
    return res


def main():
    given_arr = [1, 3, 0, 12, 11, 9, 14, 10, 15, 4, 13, 8, 5, 6, 2, 7]
    print("Given array: ", given_arr)
    sorts = [
        "bubble_sort", "insertion_sort", "selection_sort",
        "merge_sort", "quick_sort"]

    for sort in sorts:
        print("Sorting array with: ", sort)
        sorted_arr = locals()[sort](__copy(given_arr))
        print("Sorted array: ", sorted_arr)


if __name__ == '__main__':
    main()