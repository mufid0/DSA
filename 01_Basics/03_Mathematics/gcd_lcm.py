def gcd(a, b):
    """Compute GCD using Euclidean Algorithm"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute LCM using GCD"""
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    print("GCD:", gcd(12, 18))
    print("LCM:", lcm(12, 18))
    