#======== Factorial Program ========

'''
Factorial of non-negative integers n,denoted by n! is the
product of all positive integers less then or equal to n.
'''

# ====== In-Built Function for factorial ========

import math
inp = int(input("Enter number \n"))

result = math.factorial(inp)
print(result)




# ==== Recursive manner =====

def factorial_recursive(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*factorial_recursive(n-1)

print(factorial_recursive(1))

# ====== Iterative Manner ========

def factorial_iterative(n):
    result = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            result = result*i
    return result

print(factorial_iterative(3))

