def is_prime(n):
    """Check if number is prime"""
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


if __name__ == "__main__":
    print(is_prime(7))   # True
    print(is_prime(10))  # False
    