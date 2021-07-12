#========= Perfect Numbers ==========

'''
Perfect Numbers : Perfect number is a positive integer that is equal to the sum of its positive 
divisors exculding the number itself.

OR

Perfect number is a positive integer that is equal to the half of the sum of its all positive divisors.

'''

def isPerfect(num):
    result = 0
    for i in range(1,num):
        if num % i == 0:
            result = result + i
    if result == num:
        return True
    else:
        return False

def print_perfect_numbers(n):
    for i in range(1,n+1):
        if isPerfect(i):
            print(i,end =" ")

print_perfect_numbers(1000)
