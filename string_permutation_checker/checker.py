# checker.py

from collections import Counter

def are_permutations(str1: str, str2: str) -> bool:
    """
    Check if two strings are permutations of each other.
    
    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    
    Returns:
        bool: True if str1 is a permutation of str2, False otherwise.
    """
    # Step 1: Check if lengths are the same
    if len(str1) != len(str2):
        return False
    
    # Step 2: Compare character counts
    return Counter(str1) == Counter(str2)
