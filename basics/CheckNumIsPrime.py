def is_prime(n):
    """
    Check if a number is prime.
    Returns True if the number is prime, False otherwise.
    """
    try:
        # Convert to integer if string is passed
        n = int(n)
        
        # Handle edge cases
        if n <= 1:
            return False
            
        # Check for divisibility
        if n <= 3:
            return True
            
        # Skip even numbers and optimized checking
        if n % 2 == 0 or n % 3 == 0:
            return False
            
        # Check using 6k±1 optimization
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
            
        return True
        
    except ValueError:
        # Handle non-integer inputs
        return None

def display_prime_result(n):
    """Display the result of the prime check in a user-friendly format"""
    result = is_prime(n)
    
    if result is None:
        print(f"'{n}' is not a valid number")
    elif result:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

def main():
    n = input('Enter any number: ')
    display_prime_result(n)

if __name__ == "__main__":
    main()
