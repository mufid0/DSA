# Array Basics in Python

# Traverse: Iterate through the array and print each element.
def traverse(arr):
    for x in arr:
        print(x)

# Search: Find the index of a specific value in the array. Return -1 if not found.
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Insert: Add a new value at a specific index in the array.
def insert(arr, index, value):
    arr.insert(index, value)
    return arr

# Delete: Remove a specific value from the array. If the value is not found, do nothing.
def delete(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    print("Traverse:")
    traverse(arr)

    print("Search 3:", search(arr, 3))

    print("Insert 10 at index 2:", insert(arr, 2, 10))

    print("Delete 4:", delete(arr, 4))
