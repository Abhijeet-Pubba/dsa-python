"""
Problem: Print every digit of a given integer, one digit per line.
"""

def extract_digits(integer: int) -> None:
    """Print each digit of an integer, starting from the last digit.

    Args:
        integer: The number whose digits should be printed.

    Returns:
        None. The digits are printed, not returned.
    """
    number = integer
    if number == 0:
        print(0)
    while number > 0:
        last_digit = number % 10
        print(last_digit)
        number = number // 10


"""
Explanation
-----------
The loop uses two operations:

    number % 10    gives the last digit    (1234 % 10 = 4)
    number // 10   removes the last digit  (1234 // 10 = 123)

Each pass prints one digit and removes it. The loop stops when number becomes 0.

Trace for integer = 1234:

    number = 1234  ->  print 4, number = 123
    number = 123   ->  print 3, number = 12
    number = 12    ->  print 2, number = 1
    number = 1     ->  print 1, number = 0

Because we always take the digit from the right end, the digits are printed
in reverse order: 4 3 2 1.

0 is handled by its own check, so it prints 0. Negative numbers never enter
the loop, so nothing is printed for them.
"""

"""
Complexity
----------
Time:  O(log 10 N), where N is the integer.
Space: O(1)
"""

if __name__ == "__main__":
    extract_digits(1234)
