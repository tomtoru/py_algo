from concurrent.futures import process
import random
import time
from typing import List, Any, Optional


def in_order(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers) - 1))
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True

def test_sort_speed(sort_func: Any, numbers: List[int]) -> Optional[float]:
    start = time.time()
    sorted_nums = sort_func(numbers)
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
            if numbers[j] > numbers[j +1]:
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


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(1000)]

    # print('bogo_sort:', test_sort_speed(bogo_sort, nums))
    print('bubble_sort:\n', test_sort_speed(bubble_sort, nums))
    print('cocktail_sort:\n', test_sort_speed(cocktail_sort, nums))
    print('comb_sort:\n', test_sort_speed(comb_sort, nums))
