import random

# Generating a random Array to be sorted
# If needed, the random elements assignment could be removed, so a chosen array could be sorted
ArrayToBeSorted = [random.randint(-100, 100) for item in range(15)]

def MergeSort (array, left_index, right_index):
    if left_index >= right_index:
        return
    
    middle = (left_index + right_index) // 2
    MergeSort(array, left_index, middle)
    MergeSort(array, middle + 1, right_index)
    Merge(array, left_index, right_index, middle)


def Merge(array, left_index, right_index, middle):
    # Make copies of each half of the initial array
    left_array = array[left_index:middle + 1]
    right_array = array[middle + 1:right_index + 1]

    # Track the position we're in in both halves of the array (left and right arrays)
    left_array_index = 0
    right_array_index = 0
    sorting_index = left_index

    #Go through the elements of each array until we've run out of elements in any of them
    while left_array_index < len(left_array) and right_array_index < len(right_array):
        
        # The smallest element between the left and right arrays will be placed in the original array
        if left_array[left_array_index] <= right_array[right_array_index]:
            array[sorting_index] = left_array[left_array_index]
            left_array_index += 1
        else:
            array[sorting_index] = right_array[right_array_index]
            right_array_index += 1

        # After we've sorted an element, we increment the position so we can add the other elements    
        sorting_index += 1

    # After we've run our of elements in the arrays, we check for any elements that might have been left out
    while left_array_index < len(left_array):
        array[sorting_index] = left_array[left_array_index]
        left_array_index += 1
        sorting_index += 1
    
    while right_array_index < len(right_array):
        array[sorting_index] = right_array[right_array_index]
        right_array_index += 1
        sorting_index += 1


print(ArrayToBeSorted)
MergeSort(ArrayToBeSorted, 0, len(ArrayToBeSorted) - 1)
print(ArrayToBeSorted)