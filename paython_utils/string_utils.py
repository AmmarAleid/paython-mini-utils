def reverse_string(text: str) -> str:
    """
    Reverse a given string.

    Args:
        text: The input string.

    Returns:
        The reversed version of the input string.
    """
    return text[::-1]


def count_vowels(text: str) -> int:
    """
    Count how many vowels are in a string.

    Args:
        text: The input string.

    Returns:
        The number of vowels found in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
