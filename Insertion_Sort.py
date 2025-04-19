arr = [7, 1, 4, 5, 3, 2, 1]

for i in range(1, len(arr)):

  current = arr[i]
  j = i - 1

  while (j >= 0) and (current < arr[j]):
    arr[j+1] = arr[j]
    j = j - 1
  
  arr[j+1] = current

print(arr)


# Output
# [1, 1, 2, 3, 4, 5, 7]