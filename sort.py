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


def bucket_sort(numbers: List[int], bucket_size: int = 100) -> List[int]:
    """
    1. create any buckets
    2. Assign numbers to each bucket according to the size of the number
    3. sort by each bucket
    4. merge buckets
    """
    buckets = [[] for _ in range(bucket_size)]
    for num in numbers:
        # HACK:: improvement to define bucket_i
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


def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2
    while gap > 0:
        for i in range(gap, len_numbers):
            tmp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap] > tmp:
                numbers[j] = numbers[j-gap]
                j -= gap

            numbers[j] = tmp

        gap //= 2

    return numbers


def count_sort(numbers: List[int]) -> List[int]:
    count_list = [0] * (max(numbers) + 1)
    result = [0] * len(numbers)
    # count appearances of number
    for num in numbers:
        count_list[num] += 1
    # get index list(calicuate cumulative number of appearances)
    sum_count = 0
    i = 0
    for count in count_list:
        sum_count += count
        count_list[i] = sum_count
        i += 1
    # relocation
    for num in numbers:
        idx = count_list[num] - 1
        count_list[num] = count_list[num] - 1
        result[idx] = num

    return result


def count_sort_by_specified_digit(numbers: List[int], digit: int) -> List[int]:
    count_list = [0] * 10
    result = [0] * len(numbers)
    for num in numbers:
        idx = int(num / digit) % 10
        count_list[idx] += 1

    sum_count = 0
    i = 0
    for count in count_list:
        sum_count += count
        count_list[i] = sum_count
        i += 1

    for num in numbers[::-1]:
        idx = int(num / digit) % 10
        result[count_list[idx] - 1] = num
        count_list[idx] -= 1

    return result


def radix_sort(numbers: List[int]) -> List[int]:
    """
    sort by digit
    """
    max_num = max(numbers)
    digit = 1
    while max_num >= digit:
        numbers = count_sort_by_specified_digit(numbers, digit)
        digit *= 10

    return numbers


def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_idx = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_idx-1)
            _quick_sort(numbers, partition_idx+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


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
    print('shell_sort:\n', test_sort_speed(shell_sort, nums))
    print('count_sort:\n', test_sort_speed(count_sort, nums))
    print('radix_sort:\n', test_sort_speed(radix_sort, nums))
    print('quick_sort:\n', test_sort_speed(quick_sort, nums))
    print('merge_sort:\n', test_sort_speed(merge_sort, nums))
