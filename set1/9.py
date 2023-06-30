def generate_fibonacci(n):
    fibonacci_seq = [0, 1]  

    # Generate the Fibonacci sequence
    for i in range(2, n):
        fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])

    return fibonacci_seq[:n]

# Example usage
n = 5
result = generate_fibonacci(n)
print(result)
