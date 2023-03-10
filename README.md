The script has recursive functions that calculate the value of the nth term in the Fibonacci sequence where n is the user input. The three laws of recursion are established as follows:
-	Base case: if n <=2, then result = 1
-	Moving towards the base case: f(n-1) and f(n-2).
-	The recursive call: return f(n-1) + f(n-2).

Through an analysis of the algorithmic efficiency, i.e. complexity of the code, in terms of execution time represented by the Big-O notation, we can observe the following: 
The “fibonacci_recursive” function
The first statement for the base case has one constant complexity operation O(1) as this always returns the same value (1) regardless of the input when the base condition is reached.
The second statement has recursive calls in the return statement, which makes it the most dominant operation required to execute this function. As the value of the input (n) increases, the required number of function calls to reach the base case rapidly increases, and as each function call makes two recursive calls (once for n-1 and another for n-2), the rate is 2n . Therefore, this function can be represented by an exponential order of magnitude of O(2n). Considering the worst case for the input, there is no limit on the value that the user can provide. However, if we assume that the maximum allowed recursive calls is 1000, then by theory we can consider this as the worst case, making the average case almost half of this value. Yet, the exponential nature of this function’s complexity makes this it inefficient even for input values much less than this. For example, an input value of 20 will produce more (2)30 steps which is more than one billion operations. We can therefore deduce that this recursive function is inefficient for most input values and will consume considerable computation time. 
An iterative solution, on the other hand, will include a loop of n times adding the result of (n-1) and (n-2) to the result. The big-O notation for the complexity of the iterative option is therefore O(n) i.e. Linear and would be considerably faster for bigger values.

The “fibonacci_caching” function
Alternatively, if caching is used as discussed in chapter 5.12 of the textbook to store the results of function calls in a dictionary, then the stored values can be retrieved rather than recalculated when branching down calls. As each function call will only be made once, there will be almost n calls for an input n. The complexity representation of this function will therefore be linear with an order of magnitude of O(n). This solution is represented in the fibonacci_caching function in the code and is much more efficient that the first function.
For comparison, for an input of n=40, the recorded times during writing this code are shown in the snapshot below:
 

It is worth to note that in terms of space complexity, the amount of memory allocation required of both functions does not represent a concern. The reason is that it is directly proportional to the maximum depth of the recursion, i.e. linear, as each call is reserved on the recursion stack. 
