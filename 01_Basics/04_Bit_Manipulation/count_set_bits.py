"""
Count Set Bits (Number of 1s in Binary Representation)
-----------------------------------------------------
Includes multiple approaches for learning and optimization.
"""

def count_set_bits(n: int) -> int:
    """
    Count set bits using basic method
    Time Complexity: O(log n)
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def count_set_bits_kernighan(n: int) -> int:
    """
    Brian Kernighan’s Algorithm
    Removes the lowest set bit in each iteration
    Time Complexity: O(number of set bits)
    """
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count


def count_set_bits_builtin(n: int) -> int:
    """
    Python built-in method
    Fast and simple
    """
    return bin(n).count('1')


if __name__ == "__main__":
    n = 13  # binary: 1101

    print("Number:", n)
    print("Binary:", bin(n))

    print("Set bits (basic):", count_set_bits(n))
    print("Set bits (Kernighan):", count_set_bits_kernighan(n))
    print("Set bits (built-in):", count_set_bits_builtin(n))