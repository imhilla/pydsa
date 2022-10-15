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

print(factorial(4))

# Divide and conquer
# one of the important and effective techniques 
# for solving a complex problem is divide and conquer
# the divide and conquer paradigm divides a problem
# into smaller sub-problems
# and then solves these: finally it combines the result
# to obtain a global optimal solution.
