
import heapq

from misc.file_utils import read_input_dataset
from os import getenv


class MaxHeapObj(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class MinHeap(object):
    def __init__(self):
        self.h = []

    def heappush(self, x):
        heapq.heappush(self.h, x)

    def heappop(self):
        return heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i]

    def __len__(self):
        return len(self.h)


class MaxHeap(MinHeap):
    def heappush(self, x):
        heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self):
        return heapq.heappop(self.h).val

    def __getitem__(self, i):
        return self.h[i].val


def calculate_medians(numbers):
    max_objects = MaxHeap()  # contains all numbers lt/le than median
    min_objects = MinHeap()  # contains all numbers gt/ge than median
    medians = []

    max_objects.heappush(min(numbers[0], numbers[1]))
    min_objects.heappush(max(numbers[0], numbers[1]))

    # add first two numbers to list of medians. median for the list of single
    # number is a number itself, median for the list of two numbers is the
    # second number according to formula: if n is odd, then median n is the
    # (n+1/2)'th smallest number, if n is even, then median n is the (n/2)'th
    # smallest number
    medians.append(max_objects[0])
    medians.append(min_objects[0])

    processed_numbers = 2
    for i in range(2, len(numbers)):
        next_number = numbers[i]

        # if number is lt/le than the max of maxheap, then add to maxheap
        if next_number < max_objects[0]:
            max_objects.heappush(next_number)
        # if number is gt/ge than the min of minheap, then add to minheap
        elif next_number >= min_objects[0]:
            min_objects.heappush(next_number)
        # if number is between max of maxheap and min of minheap,
        # add to heap with smaller number of elements
        else:
            if len(min_objects) > len(max_objects):
                max_objects.heappush(next_number)
            else:
                min_objects.heappush(next_number)

        # rebalance minheap and maxheap if their size differs more than 1
        if len(min_objects) - len(max_objects) > 1:
            max_objects.heappush(min_objects.heappop())
        elif len(max_objects) - len(min_objects) > 1:
            min_objects.heappush(max_objects.heappop())

        # if n is odd, take smallest element from right part of array,
        # if n is even, take biggest element from left part of array
        median = 0
        if len(max_objects) == len(min_objects):
            median = max_objects[0]
        elif len(max_objects) > len(min_objects):
            median = max_objects[0]
        else:
            median = min_objects[0]
        medians.append(median)
        processed_numbers += 1

    return medians


def main():
    numbers = read_input_dataset(
        '{}/{}/'.format(getenv('BASE_DIR'), 'course2/week3'),
        'Median.txt')

    medians = calculate_medians(numbers)
    medians_sum = 0
    for next_median in medians:
        medians_sum += next_median
    medians_sum %= 10000
    print(medians[:10])
    print(medians_sum)


if __name__ == '__main__':
    main()
