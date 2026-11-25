"""
Problem: Given a string s and a list of characters, print how many times each
character in the list appears in s.

Three versions, depending on the characters allowed:
    1. Lowercase letters only (a-z)
    2. ASCII characters (0 to 127)
    3. Any characters (dict)
"""


def count_occurrences_with_array(string: str, char_list: list[str]) -> None:
    """Prints how many times each character in char_list appears in string.

    Constraint: string and every character in char_list must be 'a' to 'z'.

    Args:
        string (str): The string to count characters in.
        char_list (list[str]): The characters to look up.

    Returns:
        None. The results are printed.
    """
    count_array = [0] * 26
    for char in string:
        count_array[ord(char) - ord("a")] += 1
    for char in char_list:
        print(f"{char} -> {count_array[ord(char) - ord('a')]}")


"""
Complexity (count_occurrences_with_array)
-----------------------------------------
Time:  O(n + m), where n = len(string) and m = len(char_list)
Space: O(1), the array size is fixed at 26
"""


def count_occurrences_with_ascii_array(string: str, char_list: list[str]) -> None:
    """Prints how many times each character in char_list appears in string.

    Constraint: string and every character in char_list must be ASCII (0 to 127).

    Args:
        string (str): The string to count characters in.
        char_list (list[str]): The characters to look up.

    Returns:
        None. The results are printed.
    """
    count_array = [0] * 128
    for char in string:
        count_array[ord(char)] += 1
    for char in char_list:
        print(f"{char} -> {count_array[ord(char)]}")


"""
Complexity (count_occurrences_with_ascii_array)
-----------------------------------------------
Time:  O(n + m), where n = len(string) and m = len(char_list)
Space: O(1), the array size is fixed at 128
"""


def count_occurrences_with_dict(string: str, char_list: list[str]) -> None:
    """Prints how many times each character in char_list appears in string.

    Constraint: none. Works for any characters, including Unicode.

    Args:
        string (str): The string to count characters in.
        char_list (list[str]): The characters to look up.

    Returns:
        None. The results are printed.
    """
    count_map = {}
    for char in string:
        count_map[char] = count_map.get(char, 0) + 1
    for char in char_list:
        print(f"{char} -> {count_map.get(char, 0)}")


"""
Complexity (count_occurrences_with_dict)
----------------------------------------
Time:  O(n + m) on average, where n = len(string) and m = len(char_list)
Space: O(u), where u is the number of distinct characters in string
"""


if __name__ == "__main__":
    s = "azyxyyzaaaa"
    q = ["d", "a", "y", "x"]
    count_occurrences_with_array(s, q)

    s = "azyxyyzaaaaAABBHHFTHKJSKJJKBJSVG "
    q = ["d", "a", "y", "x", "A", "L", "=", " "]
    count_occurrences_with_ascii_array(s, q)
    count_occurrences_with_dict(s, q)
