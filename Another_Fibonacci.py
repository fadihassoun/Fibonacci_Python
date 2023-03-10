"""
Author: Fadi Hassoun - North Wales Management School, Wrexham Glyndŵr University.


Description: A recursive code to calculate the nth term in the Fibonacci sequence. The code accepts a positive
integer as an input from the user, and outputs the nth term of the sequence. It is assumed that the sequence starts
with F(1), i.e: 1, 1, 2, 3, 5, 8, 13, 21… .

"""
import time


# The getting input from user function.
def get_input():
    return input("\nPlease enter a positive integer to get its corresponding term in the Fibonacci sequence: ")


# Input validation function to check if the input is digits (without floating points or the negative sign) and not 0.
def valid_input(n):
    if not n.isdigit() or int(n) == 0:
        print("The input provided is invalid")
        return False
    else:
        return True


# The Fibonacci function using recursion.
def fibonacci_recursive(n):
    # The first and second term have a value of 1 (base case).
    if 0 < n <= 2:
        return 1
    # The remaining terms' values are the addition of the previous two results (recursive calls).
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


# The Fibonacci function using recursion and caching, the caching is done with the use of a dictionary where the keys
# are the term positions and the values are their corresponding values.
def fibonacci_caching(n, stored_results={}):
    # The first and second term have a value of 1 (base case).
    if 0 < n <= 2:
        return 1
    # check if the result has been previously stored and returns its value if exists
    elif n in stored_results:
        return stored_results[n]
    # Otherwise, the result should be the addition of the previous two results (recursive calls)
    else:
        stored_results[n] = fibonacci_caching(n - 2, stored_results) + fibonacci_caching(n - 1, stored_results)
        return stored_results[n]


# Testing the results of F1 to F8, the result should be 1, 1, 2, 3, 5, 8, 13, 21. (Uncomment the next two lines to test)

# print("The first 8 terms of the Fibonacci sequence using the fibonacci_recursive function are:",
#       fibonacci_recursive(1), fibonacci_recursive(2), fibonacci_recursive(3), fibonacci_recursive(4),
#       fibonacci_recursive(5), fibonacci_recursive(6), fibonacci_recursive(7), fibonacci_recursive(8))

# print("The first 8 terms of the Fibonacci sequence using the fibonacci_caching function are:", fibonacci_caching(1),
#       fibonacci_caching(2), fibonacci_caching(3), fibonacci_caching(4), fibonacci_caching(5), fibonacci_caching(6),
#       fibonacci_caching(7), fibonacci_caching(8))

# Getting the user input and storing it n
n = get_input()
# checking if the input is valid, and asking the user for new input until it is valid
while not valid_input(n):
    n = get_input()

# Results with simple time calculations for the operations
start = time.time()
print(f"\nTerm {n} of the Fibonacci sequence using recursion is:", fibonacci_recursive(int(n)))
end = time.time()
print('The result using recursion was calculated in: ', (end - start), 'seconds')

start = time.time()
print(f"\nTerm {n} of the Fibonacci sequence using recursion with caching is:", fibonacci_caching(int(n)))
end = time.time()
print('The result using recursion with caching was calculated in: ', (end - start), 'seconds')

