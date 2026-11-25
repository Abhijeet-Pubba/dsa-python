"""
Problem: Given two lists lst_1 and lst_2, print how many times each element
of lst_2 appears in lst_1.

Constraint: every value is between 1 and 10.

    lst_1 = [1, 2, 3, 3]
    lst_2 = [3, 6]
    output: 3 -> 2, 6 -> 0
"""


def count_occurrences_with_array(lst_1: list[int], lst_2: list[int]) -> None:
    """Prints how many times each element of lst_2 appears in lst_1.

    Uses a fixed-size array as a hash table: the index is the value and the
    stored number is its count. Only works for values from 1 to 10.

    Args:
        lst_1 (list[int]): The list to count occurrences in.
        lst_2 (list[int]): The values to look up.

    Returns:
        None. The results are printed.
    """
    count_array = [0] * 11
    for value in lst_1:
        count_array[value] += 1
    for value in lst_2:
        if value < 1 or value > 10:
            print(f"{value} -> 0")
        else:
            print(f"{value} -> {count_array[value]}")


"""
Complexity (count_occurrences_with_array)
-----------------------------------------
Time:  O(n + m), where n = len(lst_1) and m = len(lst_2)
Space: O(1), the array size is fixed at 11
"""


def count_occurrences_with_dict(lst_1: list[int], lst_2: list[int]) -> None:
    """Prints how many times each element of lst_2 appears in lst_1.

    Uses a dictionary as a hash table, so it works for any hashable values,
    not just 1 to 10. Use this when there is no fixed range.

    Args:
        lst_1 (list): The list to count occurrences in.
        lst_2 (list): The values to look up.

    Returns:
        None. The results are printed.
    """
    count_map = {}
    for value in lst_1:
        count_map[value] = count_map.get(value, 0) + 1
    for value in lst_2:
        print(f"{value} -> {count_map.get(value, 0)}")


"""
Complexity (count_occurrences_with_dict)
----------------------------------------
Time:  O(n + m) on average, where n = len(lst_1) and m = len(lst_2)
Space: O(u), where u is the number of distinct values in lst_1
"""


if __name__ == "__main__":
    lst_1 = [1, 2, 3, 3, 4, 4, 7, 3, 9, 10, 5, 5, 5, 5, 7, 8, 8]
    lst_2 = [3, 6, 11, 34, 0, 4, 111, 5, 2, 98]
    count_occurrences_with_array(lst_1, lst_2)
    count_occurrences_with_dict(lst_1, lst_2)
