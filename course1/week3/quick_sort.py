

from enum import Enum
from misc.file_utils import read_input_dataset
from misc.sort_utils import copy, swap, is_sorted


class PivotType(Enum):
    FIRST = 1
    LAST = 2
    MEDIAN = 3


class Counter:
    def __init__(self, n=0):
        self.total = n

    def __call__(self, x=0):
        self.total += x


def quick_sort(array, lo=0, hi=None, pivot_type=PivotType.FIRST, counter=None):
    if hi is None:
        hi = len(array) - 1

    if lo < hi:
        pivot_idx = __qs_partition(array, lo, hi, pivot_type, counter)
        quick_sort(array, lo, pivot_idx - 1, pivot_type, counter)
        quick_sort(array, pivot_idx + 1, hi, pivot_type, counter)


def __qs_partition(array, lo, hi, pivot_type, counter):
    # select an element of array(leftmost) as a pivot then go through array
    # and move all elements smaller than pivot to the left and greater
    # to the right
    pivot_idx = __resolve_pivot(array, lo, hi, pivot_type)
    pivot = array[pivot_idx]
    # swap pivot with leftmost element as partition algorithm is adapted
    # to leftmost value as a pivot
    swap(array, lo, pivot_idx)

    if counter:
        counter(hi - lo)

    i = lo + 1
    for j in range(lo + 1, hi + 1):

        if array[j] < pivot:
            swap(array, i, j)
            # after each swap operation there is one more element
            # smaller than pivot.
            i += 1
    # i represents number of swaps made and next position of pivot element
    swap(array, lo, i - 1)
    return i - 1


def __resolve_pivot(array, lo, hi, pivot_type):
    types = {
        PivotType.FIRST: lo,
        PivotType.LAST: hi,
        PivotType.MEDIAN: __resolve_median(array, lo, hi)
    }
    return types[pivot_type]


def __resolve_median(array, lo, hi):
    med = (hi - lo) // 2 + lo
    val2idx = {
        array[lo]: lo,
        array[med]: med,
        array[hi]: hi
    }
    values = sorted([array[lo], array[med], array[hi]])
    median = val2idx[values[1]]
    return median


def main():
    # given_arr = [1, 3, 0, 9, 4, 8, 5, 6, 2, 7]
    # given_arr = [1, 3, 0, 12, 11, 9, 14, 10, 15, 4, 13, 8, 5, 6, 2, 7]
    given_arr = read_input_dataset(
        '/mnt/c/work/projects/algorithms-stanford/course1/week3/',
        'QuickSort.txt')

    # print("Given array: ", given_arr)

    for pivot_type in PivotType:
        array = copy(given_arr)
        counter = Counter()
        quick_sort(array, pivot_type=pivot_type, counter=counter)
        print("Array is {}, comparisons count: {}".format(
            is_sorted(array), counter.total))


if __name__ == '__main__':
    main()
