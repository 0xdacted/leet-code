# Given an array containing 0s, 1s and 2s, sort the array in-place. 
# You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; 
# and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

def dutch_flag_sort(arr):
  left, right = 0, len(arr) - 1
  i = 0

  while i <= right:
    if arr[i] == 0:
      arr[i], arr[low] = arr[low], arr[i]
      i += 1
      low += 1
    elif arr[i] == 2:
      arr[i], arr[high] = arr[high], arr[i]
      high -= 1
    else:
      i += 1
  return arr




