#========= GCD of two Numbers =========

'''
GCD --> Greatest Common Divisor 
OR
HCF --> Highest Common Factor 
Both are same.

'''

# ===>> Using inbuild Function

import math
z = math.gcd(48,15)
print(z)


# ===>> Using Iterative Method
x = 48
y = 64
list1 = []
list2 = []
list3 = []
for i in range(1,x+1):
    if x % i == 0:
        list1.append(i)
# print(list1)
for j in range(1,y+1):
    if y % j == 0:
        list2.append(j)
# print(list2)
for item in list1:
    if item in list2:
        list3.append(item)
print(list3)
print(max(list3))


#=====>> Using Euclid's Algorithm

def HCF(a,b):
   
    if a<b :
        result = a
        while a != 0:
            y = b % a
            b = a
            a = y
        result = b
    else:
        result = b
        while b != 0:
            y = a % b
            a = b
            b = y
        result = a
    return result
print()
print(HCF(15,48))

# ====>> Using Recursion

def ComputeHCF(a,b):
    if b == 0:
        return a
    else:
        return ComputeHCF(b,a%b)

print(ComputeHCF(48,15))