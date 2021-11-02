# Helpful steps/hints 
    # Iterate over the unsorted list. Make sure to keep track of the minimum value's position throughout.
    # When at the end of the list, we should know which element is the minimum value.
    # Swap the minimum element and the first element in the unsorted list.
    # The first element is now sorted.
    # Repeat this process until the entire list is sorted.

def selection_sort(lst): 
    for i in range(0, len(lst) - 1):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                # change the minimum number's position if a smaller number is identified
                min = j
        
        # after each pass through the items in the list, if the current minimum number is not equal 
        # to the minimum number (min), then exchange positions and swap numbers
        if min != i: 
            lst[i], lst[min] = lst[min], lst[i]

    return lst


sample_list = [5, 8, 1, 22, 18, 6, 2]
print(f"Unsorted list: {sample_list}")
selection_sort(sample_list)
print(f"Sorted list: {sample_list}")