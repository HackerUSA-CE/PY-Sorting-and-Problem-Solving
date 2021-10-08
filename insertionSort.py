# Helpful hints:
# Define a function named 'insertion_sort' that takes in an unsorted numerical list as an argument, 'test_list'.
# Write a for loop that loops through the number of times that there are elements.
# Set a variable called 'current_value' equal to the value at index 'i' in 'test_list' (note that 'i' here is the variable that is being incremented, if you used a different variable than use that in this step). This will be the element to be compared.
# Compare the current element with the sorted portion. Write a while loop that runs while 'i' is greater than 0 and the value of the element of the list at index 'i-1' is greater than the current value.
#     In the while loop, set the value of the element at index 'i' equal to the value of the element at index 'i-1'. Set 'i' equal to 'i-1'. Set the element at index 'i' equal to 'current_value'.


def insertion_sort(test_list):

    for i in range(1, len(test_list)):
        current_value = test_list[i]

        while i > 0 and test_list[i-1] > current_value:
            test_list[i] = test_list[i - 1]
            i = i - 1
            test_list[i] = current_value

        # uncomment the line below to view how the list is being sorted
        # print(test_list)
    return test_list

sample_list = [5, 8, 1, 22, 18, 6, 2]
print(f"Unsorted list: {sample_list}")
insertion_sort(sample_list)
print(f"Sorted list: {sample_list}")