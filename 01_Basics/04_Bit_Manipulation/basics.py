"""
Basic Bit Manipulation Operations
--------------------------------
Covers fundamental bitwise operations used in DSA.
"""

def is_even(n: int) -> bool:
    """Check if a number is even using bitwise AND"""
    return (n & 1) == 0


def is_odd(n: int) -> bool:
    """Check if a number is odd"""
    return (n & 1) == 1


def multiply_by_2(n: int) -> int:
    """Multiply a number by 2 using left shift"""
    return n << 1


def divide_by_2(n: int) -> int:
    """Divide a number by 2 using right shift"""
    return n >> 1


def check_kth_bit(n: int, k: int) -> bool:
    """Check if k-th bit (0-indexed) is set"""
    return (n & (1 << k)) != 0


def set_kth_bit(n: int, k: int) -> int:
    """Set the k-th bit"""
    return n | (1 << k)


def clear_kth_bit(n: int, k: int) -> int:
    """Clear the k-th bit"""
    return n & ~(1 << k)


def toggle_kth_bit(n: int, k: int) -> int:
    """Toggle the k-th bit"""
    return n ^ (1 << k)


if __name__ == "__main__":
    n = 5  # binary: 101

    print("Number:", n)
    print("Is Even:", is_even(n))
    print("Is Odd:", is_odd(n))
    print("Multiply by 2:", multiply_by_2(n))
    print("Divide by 2:", divide_by_2(n))

    k = 1
    print(f"Check {k}-th bit:", check_kth_bit(n, k))
    print(f"Set {k}-th bit:", set_kth_bit(n, k))
    print(f"Clear {k}-th bit:", clear_kth_bit(n, k))
    print(f"Toggle {k}-th bit:", toggle_kth_bit(n, k))