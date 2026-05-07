# Basic problems related to arrays

# Find the maximum element in an array
def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

# Reverse an array in place
def reverse(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Check if an array is sorted in non-decreasing order
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Remove duplicates from a sorted array and return the new length of the array
def remove_duplicates(arr):
    if not arr:
        return 0
    # Initialize the index of the last unique element
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    # The length of the array with unique elements is i + 1
    return i + 1

# Move all zeros in an array to the end while maintaining the order of non-zero elements
def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr