"""
Problem: Given an integer, return true if integer is a palindrome, and false otherwise.

    121   -> True
    10    -> False
"""

def check_palindrome(integer):
    """Checks whether an integer is a palindrome.

    Args:
        integer (int): The number to check.

    Returns:
        bool: True if the number is palindrome, False otherwise.
    """
    number = integer
    reversed = 0
    while number > 0:
        last_digit = number % 10
        reversed = (reversed * 10) + last_digit
        number = number // 10
    return integer == reversed


"""
Complexity
----------
Time:  O(log 10 N)
Space: O(1)
"""

if __name__ == "__main__":
    print(check_palindrome(121))
