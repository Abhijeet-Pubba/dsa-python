"""
Problem: Check whether a positive integer is an Armstrong number. A number is
Armstrong if it equals the sum of its digits, each raised to the power of the
number of digits.

    153   -> True    (1^3 + 5^3 + 3^3 = 153)
    372   -> False   (3^3 + 7^3 + 2^3 = 378)
    1634  -> True    (1^4 + 6^4 + 3^4 + 4^4 = 1634)
"""

def is_amstrong(integer):
    """Checks whether an integer is an Armstrong number.

    Args:
        integer (int): The positive integer to check.

    Returns:
        bool: True if the number is amstrong, False otherwise.
    """
    no_of_digits = len(str(integer))
    number = integer
    total = 0
    while number > 0:
        last_digit = number % 10
        total = total + last_digit ** no_of_digits
        number = number // 10
    return total == integer


"""
Complexity
----------
Time:  O(log10 N)
Space: O(1)
"""

if __name__ == "__main__":
    print(is_amstrong(153))
