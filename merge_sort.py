#MERGE SORT
# --> DIVIDE AND CONQUER ALGORITHM

def MergeSort(array):
  if len(array) > 1:
    # Split Operation
    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]

    MergeSort(left_array)
    MergeSort(right_array)

    # Sort Operation
    left_array_pointer = 0
    right_array_pointer = 0
    final_array_pointer = 0

    while ((left_array_pointer < len(left_array)) and (right_array_pointer < len(right_array))):
      if left_array[left_array_pointer] < right_array[right_array_pointer]:
        array[final_array_pointer] = left_array[left_array_pointer]
        left_array_pointer += 1
      
      else:
        array[final_array_pointer] = right_array[right_array_pointer]
        right_array_pointer +=1
      
      final_array_pointer += 1
    
    # Merge Operation
    while left_array_pointer < len(left_array):
      array[final_array_pointer] = left_array[left_array_pointer]
      final_array_pointer += 1
      left_array_pointer +=1
    
    while right_array_pointer < len(right_array):
      array[final_array_pointer] = right_array[right_array_pointer]
      final_array_pointer += 1
      right_array_pointer += 1

array = [3, 2, 6, 7, 4, 1, 8, 9, 5]
MergeSort(array)
print(array)

# OUTPUT:
#[1, 2, 3, 4, 5, 6, 7, 8, 9]