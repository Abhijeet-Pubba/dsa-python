"""
Problem: Count the number of digits in a positive integer.

    1234    -> 4
    6       -> 1
    100000  -> 6
"""

def digits_count(integer: int):
    """ Count the number of digits in a non-negative integer.

    Args:
        integer (int): The number whose digits should be counted.
    
    Returns:
        int: Total number of digits in the integer
    """
    number = integer
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


"""
Complexity
----------
Time:  O(log 10 N)
Space: O(1)
"""

if __name__ == "__main__":
    print(digits_count(1234))