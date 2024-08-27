# test_checker.py

import unittest
from string_permutation_checker.checker import are_permutations

class TestArePermutations(unittest.TestCase):
    def test_permutations(self):
        self.assertTrue(are_permutations("abc", "bca"), "Should be True for 'abc' and 'bca'")
    
    def test_different_lengths(self):
        self.assertFalse(are_permutations("abc", "ab"), "Should be False for different lengths")
    
    def test_same_length_different_characters(self):
        self.assertFalse(are_permutations("abc", "def"), "Should be False for same length but different characters")
    
    def test_repeated_characters(self):
        self.assertTrue(are_permutations("aabbcc", "abcabc"), "Should be True for 'aabbcc' and 'abcabc'")
    
    def test_empty_strings(self):
        self.assertTrue(are_permutations("", ""), "Should be True for two empty strings")
    
    def test_case_sensitivity(self):
        self.assertFalse(are_permutations("Abc", "abc"), "Should be False for 'Abc' and 'abc' due to case sensitivity")

if __name__ == '__main__':
    unittest.main()
