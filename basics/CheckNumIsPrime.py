import unittest
from io import StringIO
import sys

class TestPrimeNumber(unittest.TestCase):
    def test_prime_numbers(self):
        """Test with numbers that are prime"""
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for num in prime_numbers:
            self.assertTrue(is_prime(num), f"{num} should be identified as prime")
    
    def test_non_prime_numbers(self):
        """Test with numbers that are not prime"""
        non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for num in non_prime_numbers:
            self.assertFalse(is_prime(num), f"{num} should be identified as non-prime")
    
    def test_negative_numbers(self):
        """Test with negative numbers (not prime by definition)"""
        negative_numbers = [-1, -2, -5, -10]
        for num in negative_numbers:
            self.assertFalse(is_prime(num), f"{num} should be identified as non-prime")
    
    def test_large_prime(self):
        """Test with a larger prime number"""
        self.assertTrue(is_prime(997), "997 should be identified as prime")
    
    def test_large_non_prime(self):
        """Test with a larger non-prime number"""
        self.assertFalse(is_prime(998), "998 should be identified as non-prime")
    
    def test_string_input(self):
        """Test with string representations of numbers"""
        self.assertTrue(is_prime("17"), "String '17' should be identified as prime")
        self.assertFalse(is_prime("20"), "String '20' should be identified as non-prime")
    
    def test_invalid_input(self):
        """Test with invalid inputs"""
        self.assertIsNone(is_prime("abc"), "Non-numeric string should return None")
        self.assertIsNone(is_prime("12.5"), "Floating point string should return None")
    
    def test_display_output(self):
        """Test the output of the display function"""
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Test prime number output
        display_prime_result(17)
        self.assertEqual(captured_output.getvalue().strip(), "17 is a prime number")
        
        # Reset and test non-prime output
        captured_output.truncate(0)
        captured_output.seek(0)
        display_prime_result(20)
        self.assertEqual(captured_output.getvalue().strip(), "20 is not a prime number")
        
        # Reset and test invalid input
        captured_output.truncate(0)
        captured_output.seek(0)
        display_prime_result("abc")
        self.assertEqual(captured_output.getvalue().strip(), "'abc' is not a valid number")
        
        # Restore stdout
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
