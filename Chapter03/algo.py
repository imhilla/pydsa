# devide and conquer
# greedy algorithms
# Dynamic programming

# Algorithm design
# formulate the problem clearly
# identify the appropriate algorithm design technique based on the structure
# of the problem for an efficient solution.

# recursion algorithms
# A recursive function calls itself in order to solve a problem.

def factorial(n):
    # test for base case
    if n == 0:
        return 1
    else:
        print(n, 'n')
        # make a calculation and a recursive call
        return n * factorial(n - 1)

# print(factorial(4))

# Divide and conquer
# one of the important and effective techniques
# for solving a complex problem is divide and conquer
# the divide and conquer paradigm divides a problem
# into smaller sub-problems
# and then solves these: finally it combines the result
# to obtain a global optimal solution.

# examples include
# 1. Binary search
# 2. Merge sort
# 3. Quick sort
# 4. Algorithm for fast multiplication
# 5. Strassen's matrix multiplicatio
# 6. Closest pair of points

# Binary search
# This algorithm is used to find a given element from a sorted list of elements


def binary_search(arr, start, end, key):
    while start <= end:
        mid = start + int((end - start) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


arr = [4, 6, 9, 13, 14, 18, 21, 24, 38]
x = 13
result = binary_search(arr, 0, len(arr)-1, x)
print(result)

# Merge sort
# merge sort is an algorithm for sorting a list
#  of n natural numbers in increasing order.
# Firstly, the given list of elements is divided iteratively
# into equal parts until each sublist contains one elemnt, and then
# these sublist are combined to create a new list in a sorted order


def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    mid_point = int(len(unsorted_list) / 2)
    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]
    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)
    return merge(half_a, half_b)


def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1

    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list


a = [11, 12, 7, 41, 61, 13, 16, 14]
print(merge_sort(a))

# Dynamic programming
# dynamic programming is the most powerful design technique for solving
# optimization problems. The basic idea of dynamic programming is based on the intuition of the divide and conquer