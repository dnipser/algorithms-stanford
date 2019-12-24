
import time

from misc.file_utils import read_input_dataset
from datetime import timedelta
from os import getenv


def find_pairs_naive(numbers):
    sum_limit = 10000
    pairs = set()

    for number_n in numbers:
        for number_m in numbers:
            if number_n != number_m and abs(number_n + number_m) <= sum_limit:
                sorted_pair = sorted([number_n, number_m])
                pairs.add((sorted_pair[0], sorted_pair[1]))
                print("pair added")
    return pairs


def find_pairs(numbers):
    sum_limit = 10000
    numbers_map = {}
    sums = set()

    for number in numbers:
        numbers_map[number] = True

    for next_sum in range(-sum_limit, sum_limit + 1):
        # print("Finding pairs for sum ", next_sum)
        for number in numbers:
            summand = next_sum - number
            if number != summand and summand in numbers_map:
                sums.add(next_sum)

    return sums


def main():
    numbers = read_input_dataset(
        '{}/{}/'.format(getenv('BASE_DIR'), 'course2/week4'),
        '2sum.txt')

    start = time.time()
    sums = find_pairs(numbers)
    end = time.time()
    print(timedelta(seconds=end-start))
    print(len(sums))


if __name__ == '__main__':
    main()
