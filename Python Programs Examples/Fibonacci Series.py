# ======== Fibonacci Numbers =========

'''
series of integer numbers here first 2 number are 0,1 and next number is sum of 2 previous numbers.
ex- 0,1,1,2,3,5,8,13...
'''

#==== Print Fibonacci series ===>>

def Fibonacci_series(num):
    if num == 1 :
        return 0
    if num == 2:
        return 1
    return Fibonacci_series(num-1) + Fibonacci_series(num-2)

# print(Fibonacci_series(5))


def Fibonacci_iterative(num): # With this function we print Fibonacci Series.
    x = 0
    y = 1

    for i in range(num):
        if i < 2:
            print(i , end = " ")
        else:
            result = x + y
            print(result, end = " ")
            x = y
            y = result

Fibonacci_iterative(10)

