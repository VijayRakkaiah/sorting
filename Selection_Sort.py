arr = [1,5, 9, 10,2, 8, 12]

for position in range(len(arr)-1):
    mini = position
    for i in range(position+1, len(arr)):
        if arr[i] < arr[mini]:
            mini = i
    arr[position], arr[mini] = arr[mini], arr[position]

print(arr)

# Output
# [1, 2, 5, 8, 9, 10, 12]