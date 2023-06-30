import math

def is_prime(number):
    if number <= 1:
        return False

    # Check divisibility from 2 up to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

# Example usage
input_number = 13
result = is_prime(input_number)
print(input_number, "is a prime number")
