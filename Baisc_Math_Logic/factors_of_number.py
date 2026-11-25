"""
Problem: Return all factors of a positive integer n in sorted order.

    10  -> [1, 2, 5, 10]
    12  -> [1, 2, 3, 4, 6, 12]
"""

from math import sqrt


def factors_brute_force(number):
    """Finds all factors by checking every number from 1 to number.

    Args:
        number (int): The positive integer to find factors of.

    Returns:
        list[int]: All factors of number, in sorted order.
    """
    result = []
    for candidate in range(1, number + 1):
        if number % candidate == 0:
            result.append(candidate)
    return result


"""
Complexity (factors_brute_force)
--------------------------------
Time:  O(N)
Space: O(d), where d is the number of factors
"""


def factors_till_half(number):
    """Finds all factors by checking up to half of number.

    No factor of number is larger than number // 2 except number itself,
    so the loop stops at number // 2 and number is added at the end.

    Args:
        number (int): The positive integer to find factors of.

    Returns:
        list[int]: All factors of number, in sorted order.
    """
    result = []
    for candidate in range(1, number // 2 + 1):
        if number % candidate == 0:
            result.append(candidate)
    result.append(number)
    return result


"""
Complexity (factors_till_half)
------------------------------
Time:  O(N)
Space: O(d), where d is the number of factors
"""


def factors_till_sqrt(number):
    """Finds all factors by checking up to the square root of number.

    Every factor below sqrt(number) pairs with a factor above it
    (factor * other = number), so each divisor found gives two factors.

    Args:
        number (int): The positive integer to find factors of.

    Returns:
        list[int]: All factors of number, in sorted order.
    """
    result = []
    for candidate in range(1, int(sqrt(number)) + 1):
        if number % candidate == 0:
            result.append(candidate)
            paired_factor = number // candidate
            if paired_factor != candidate:
                result.append(paired_factor)
    result.sort()
    return result


"""
Complexity (factors_till_sqrt)
------------------------------
Time:  O(sqrt(N) + d log d), where d is the number of factors
Space: O(d), where d is the number of factors
"""


if __name__ == "__main__":
    print(factors_brute_force(10))
    print(factors_till_half(10))
    print(factors_till_sqrt(10))
