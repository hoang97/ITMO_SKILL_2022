from operator import is_
import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_factors(self):
        self.assertEqual(set(factors(2)), {2})
        self.assertEqual(set(factors(18)), {2,3,6,9,18})
        self.assertEqual(set(factors(21)), {3,7,21})

    def test_prime(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(91))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))

    def test_vowels(self):
        self.assertEqual(set(vowels('abcde')), {'a','e'})
        self.assertEqual(set(vowels('Itmo university')), {'I','o','u','e','i'})

    def test_len(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len([1,2,3]), 3)
        self.assertEqual(len([[1],[1,2],[1,2,3]]), 3)
        self.assertEqual(len('abcde'), 5)

if __name__ == "__main__":
    unittest.main(verbosity=2)