# Helpful steps/hints:
# Define a function named 'insertion_sort' that takes in an unsorted numerical list as an argument, 'lst'.
# Write a for loop that loops through the number of times that there are elements.
# Set a variable called 'current_value' equal to the value at index 'i' in 'lst' (note that 'i' here is the variable that is being incremented, if you used a different variable than use that in this step). This will be the element to be compared.
# Compare the current element with the sorted portion. Write a while loop that runs while 'i' is greater than 0 and the value of the element of the list at index 'i-1' is greater than the current value.
#     In the while loop, set the value of the element at index 'i' equal to the value of the element at index 'i-1'. Set 'i' equal to 'i-1'. Set the element at index 'i' equal to 'current_value'.


def insertion_sort(lst):

    for i in range(1, len(lst)):
        current_value = lst[i]

        while i > 0 and lst[i-1] > current_value:
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current_value

        # uncomment the line below to view how the list is being sorted
        # print(lst)
    return lst

sample_list = [5, 8, 1, 22, 18, 6, 2]
print(f"Unsorted list: {sample_list}")
insertion_sort(sample_list)
print(f"Sorted list: {sample_list}")