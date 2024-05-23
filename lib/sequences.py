#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fibonacci_sequence = [0]
    
    if length > 1:
        fibonacci_sequence.append(1)
    
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence)

# Test the function with the required test cases
print_fibonacci(0)
# Expected: []

print_fibonacci(1)
# Expected: [0]

print_fibonacci(2)
# Expected: [0, 1]

print_fibonacci(10)
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
