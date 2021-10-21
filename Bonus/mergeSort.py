def merge_sort(lst):
  if len(lst) <= 1: 
      return lst
  else:
    middle_index = len(lst) // 2
    left = lst[:middle_index]
    right = lst[middle_index:]
    left_partition = merge_sort(left)
    right_partition = merge_sort(right)
    return merge(left_partition, right_partition) 

def merge(lst1, lst2):
  results = []
  while lst1 and lst2:
      if lst1[0] < lst2[0]:
          results.append(lst1.pop(0))
      else: 
          results.append(lst2.pop(0))

  return results + lst1 + lst2

# Code to test function
sample_list = [1, 5, 7, 6, 2]
print(f"Unsorted list: {sample_list}")
sorted_list = merge_sort(sample_list)
print(f"Sorted list: {sorted_list}")