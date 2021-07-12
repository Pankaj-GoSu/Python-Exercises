#======= Printing Prime Numbers in Given Interval ==========

'''
Prime Numbers : Prime numbers is a natural number greater than 1 that has no positive 
divisors other than 1 and itself.
'''

def isPrime(num):
    if num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True
# ======== Printing Prime Numbers in Given Interval ==>>>



def print_prime(n):
    if n < 2:
        print("range is less then 2")
    for i in range(2,n):
        if isPrime(i):
            print(i,end =" ")
print_prime(102)

