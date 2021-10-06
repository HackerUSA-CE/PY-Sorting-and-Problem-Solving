def find_pair(test_list, target):
    sorted_list = sorted(test_list)
    left = 0
    right = len(sorted_list)-1

    while left < right:
        if sorted_list[left] + sorted_list[right] == target:
            return(sorted_list[left], sorted_list[right])
        
        elif sorted_list[left] + sorted_list[right] < target:
            left = left + 1
        else: 
            right = right - 1
    
    return('no pairs sum to the target')

# sample_list = [ 3, 7, 10, 8]
sample_list = [ 3, 7, 6, 8]
print(find_pair(sample_list, 9))

        