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
