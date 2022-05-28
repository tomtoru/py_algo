import random
import copy
import time
from typing import List, Callable, Optional


def in_order(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers) - 1))

def test_sort_speed(sort_func: Callable[[List[int]], List[int]], numbers: List[int]) -> Optional[float]:
    test_list = copy.deepcopy(numbers)
    start = time.time()
    sorted_nums = sort_func(test_list)
    process_time = time.time() - start
    if in_order(sorted_nums):
        return process_time
    else:
        return None

def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len(numbers)-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers

def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True
    while gap != 1 or swapped:
        gap = int(gap // 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers-gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True

    return numbers

def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    min_idx = 0
    min_number = None
    start = 0
    while start < len_numbers:
        min_number = numbers[start]
        min_idx = start
        for i in range(start, len_numbers):
            if numbers[i] < min_number:
                min_number = numbers[i]
                min_idx = i

        if start != min_idx:
            numbers[start], numbers[min_idx] = numbers[min_idx], numbers[start]

        start += 1

    return numbers

def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    idx = 0
    while idx < len_numbers:
        if idx == 0:
            idx += 1

        if numbers[idx-1] > numbers[idx]:
            numbers[idx-1], numbers[idx] = numbers[idx], numbers[idx-1]
            idx -= 1
        else:
            idx += 1

    return numbers

def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        target_num = numbers[i]
        check_idx = i - 1
        while check_idx >= 0 and numbers[check_idx] > target_num:
            numbers[check_idx+1] = numbers[check_idx]
            check_idx -= 1

        numbers[check_idx+1] = target_num

    return numbers

def bucket_sort(numbers: List[int], bucket_size: int = 10) -> List[int]:
    buckets = [[] for _ in range(bucket_size)]
    for num in numbers:
        bucket_i = num // bucket_size
        if bucket_i < bucket_size:
            buckets[bucket_i].append(num)
        else:
            buckets[bucket_size-1].append(num)

    for i in range(bucket_size):
        insertion_sort(buckets[i])

    result = []
    for i in range(bucket_size):
        result += buckets[i]

    return result

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(1000)]

    # print('bogo_sort:\n', test_sort_speed(bogo_sort, nums))
    print('bubble_sort:\n', test_sort_speed(bubble_sort, nums))
    print('cocktail_sort:\n', test_sort_speed(cocktail_sort, nums))
    print('comb_sort:\n', test_sort_speed(comb_sort, nums))
    print('selection_sort:\n', test_sort_speed(selection_sort, nums))
    print('gnome_sort:\n', test_sort_speed(gnome_sort, nums))
    print('insertion_sort:\n', test_sort_speed(insertion_sort, nums))
    print('bucket_sort:\n', test_sort_speed(bucket_sort, nums))
