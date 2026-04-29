arr = [1, 2, 3, 4, 5]

# O(1): Constant Time Complexity
def get_first(arr):
    return arr[0]


# O(n): Linear Time Complexity
def print_all(arr):
    for x in arr:
        print(x)


# O(log n):Logarithmic Time Complexity
def halve(n):
    while n > 1:
        n //= 2
        print(n)


# O(n^2): Quadratic Time Complexity
def pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
