# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    most_common = numbers[0]

    for number in counts:
        if counts[number] > counts[most_common]:
            most_common = number

    return most_common


# Test cases
print("Problem 1:")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Expected: 3
print(most_frequent([5, 5, 2, 2, 5]))        # Expected: 5
print(most_frequent([7]))                     # Expected: 7
print(most_frequent([]))                      # Expected: None


"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because the function still needs to go through the input
  list to count each number.
- Worst-case: O(n), because each number is processed when building the
  dictionary and the dictionary is checked to find the most frequent number.
- Average-case: O(n), because dictionary lookups and updates are O(1)
  on average.
- Space complexity: O(n), because the dictionary may need to store every
  number if all numbers are unique.
- Why this approach? I used a dictionary because it allows me to efficiently
  keep track of how many times each number appears.
- Could it be optimized? This is already efficient for finding the most
  frequent element. A nested-loop solution could avoid the dictionary, but
  it would take O(n^2) time. This approach uses extra memory for faster
  performance.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


# Test cases
print("\nProblem 2:")
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Expected: [4, 5, 6, 7]
print(remove_duplicates([1, 1, 1, 1]))        # Expected: [1]
print(remove_duplicates([1, 2, 3]))           # Expected: [1, 2, 3]
print(remove_duplicates([]))                  # Expected: []


"""
Time and Space Analysis for problem 2:
- Best-case: O(n), because every element in the input list must be checked.
- Worst-case: O(n), assuming average O(1) set membership and insertion.
- Average-case: O(n), because each element is visited once and set operations
  are O(1) on average.
- Space complexity: O(n), because the seen set and result list can each grow
  based on the number of unique elements.
- Why this approach? I used a set to quickly determine whether an element has
  already been seen while using a list to preserve the original order.
- Could it be optimized? This is already efficient for this problem. I could
  avoid using the set and check the result list instead, which could reduce
  the extra data structures used, but membership checks on a list are O(n).
  That could make the total time O(n^2). The set uses extra memory to give
  faster lookup performance.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs


# Test cases
print("\nProblem 3:")
print(find_pairs([1, 2, 3, 4], 5))
# Expected: [(2, 3), (1, 4)] or equivalent

print(find_pairs([1, 2, 3, 4, 5], 6))
# Expected: [(2, 4), (1, 5)] or equivalent

print(find_pairs([1, 2, 3], 10))
# Expected: []

print(find_pairs([], 5))
# Expected: []


"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because the function processes each number once.
- Worst-case: O(n), assuming average O(1) set lookup and insertion.
- Average-case: O(n), because each number is visited once and checking the
  set is O(1) on average.
- Space complexity: O(n), because the seen set may contain all input values.
  The output list also requires space for the pairs that are found.
- Why this approach? I used a set so that I can quickly check whether the
  complement needed to reach the target has already been seen.
- Could it be optimized? This solution is an optimization over a basic
  nested-loop solution. My original approach could compare every number
  with every other number, which would take O(n^2) time and O(1) auxiliary
  space besides the output. The optimized version uses a set and reduces
  the expected time complexity to O(n), but it requires O(n) extra space.
  This is a time-space trade-off: I use more memory to get faster performance.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    if n <= 0:
        return []

    capacity = 1
    size = 0
    items = [None] * capacity

    for value in range(n):
        if size == capacity:
            old_capacity = capacity
            capacity *= 2

            print(
                f"Resizing from capacity {old_capacity} "
                f"to {capacity}. Copying {size} items."
            )

            new_items = [None] * capacity

            for i in range(size):
                new_items[i] = items[i]

            items = new_items

        items[size] = value
        size += 1

    return items[:size]


# Test cases
print("\nProblem 4:")
print(add_n_items(6))
# Expected final list: [0, 1, 2, 3, 4, 5]
# Resizes should also be printed.

print(add_n_items(1))
# Expected: [0]

print(add_n_items(0))
# Expected: []


"""
Time and Space Analysis for problem 4:
- When do resizes happen? A resize happens whenever the current number of
  elements reaches the list's capacity. Starting with capacity 1, the
  capacities grow to 2, 4, 8, 16, and so on.
- What is the worst-case for a single append? O(n). When the list is full,
  a larger list must be created and the existing elements must be copied
  into it.
- What is the amortized time per append overall? O(1). Most appends do not
  require resizing, so the occasional expensive resize is spread across
  many inexpensive append operations.
- Space complexity: O(n), because the list's capacity grows in proportion
  to the number of elements being stored. During a resize, both the old
  and new lists temporarily exist, but this is still O(n).
- Why does doubling reduce the cost overall? Doubling means resizing becomes
  less frequent as the list gets larger. Instead of resizing every time an
  element is added, extra capacity is created for many future appends.
  This spreads the copying cost across many operations and gives append an
  amortized O(1) time complexity.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result


# Test cases
print("\nProblem 5:")
print(running_total([1, 2, 3, 4]))
# Expected: [1, 3, 6, 10]

print(running_total([5]))
# Expected: [5]

print(running_total([]))
# Expected: []

print(running_total([-1, 2, -3, 4]))
# Expected: [-1, 1, -2, 2]


"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because each input value is processed once.
- Worst-case: O(n), because the function goes through the entire list once.
- Average-case: O(n), because the amount of work grows directly with the
  number of elements.
- Space complexity: O(n), because a new result list containing n running
  totals is created. The running total variable itself only uses O(1)
  additional space.
- Why this approach? I keep a running sum instead of recalculating the sum
  from the beginning of the list for every position. Each number only
  needs to be added once.
- Could it be optimized? The time complexity is already O(n), which is
  optimal because every input element must be processed. If modifying the
  original input list were allowed, the calculations could be stored
  directly in that list to reduce auxiliary space. The trade-off is that
  the original input data would be changed.
"""
