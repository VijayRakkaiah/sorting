# QUICK SORT
# --> DIVIDE AND CONQUER ALGORITHM

import random

def QuickSort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = random.choice(arr)

  left = [i for i in arr if i < pivot]
  right = [i for i in arr if i > pivot]
  middle = [i for i in arr if i == pivot]

  """
  left = []
  for i in arr:
    if i < pivot:
      left.append(i)

  right = []
  for i in arr:
    if i > pivot:
      right.append(i)

  middle = []
  for i in arr:
    if i == pivot:
      middle.append(i)
  """

  return (QuickSort(left) + middle + QuickSort(right))

arr = [3, 2, 5, 7, 9, 1, 6]
print("Before: ", arr)
print("After: ", QuickSort(arr))

# Output
# Before:  [3, 2, 5, 7, 9, 1, 6]
# After:  [1, 2, 3, 5, 6, 7, 9]