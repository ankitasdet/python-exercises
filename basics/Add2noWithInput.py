def add_two_numbers(number1, number2):
    try:
        num1 = int(number1)
        num2 = int(number2)
        return num1 + num2
    except ValueError:
        return "Invalid input. Please enter numeric values."

# For interactive use
def main():
    number1 = input('Enter first number:   ')
    number2 = input('Enter second number:  ')
    result = add_two_numbers(number1, number2)
    print('Sum of 2 numbers is:', result)

# For testing
import unittest

class TestAddTwoNumbers(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(add_two_numbers('5', '10'), 15)
        self.assertEqual(add_two_numbers('0', '0'), 0)
        self.assertEqual(add_two_numbers('-5', '5'), 0)

    def test_invalid_numbers(self):
        self.assertEqual(add_two_numbers('five', '10'), "Invalid input. Please enter numeric values.")
        self.assertEqual(add_two_numbers('5', 'ten'), "Invalid input. Please enter numeric values.")
        self.assertEqual(add_two_numbers('five', 'ten'), "Invalid input. Please enter numeric values.")

    def test_empty_input(self):
        self.assertEqual(add_two_numbers('', ''), "Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    # Uncomment one of these lines:
    main()  # For normal usage
    # unittest.main()  # For running tests
