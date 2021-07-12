#========= Armstrong Numbers =============

'''
Armstrong Numbers : Numbers of n digits which are equal to sum of nth power of its digits.
example : 153 --> here 3 digits means n = 3 now if 1^3 + 5^3 + 3^3 is equal to 153 then it is 
Armstrong numbers.
Like for 5 --> here digit is 1 so n = 1 and 5^1 is equal to 5 so it is Armstrong number.
'''

# Print Armstrong Number from 0 to 1000


# def isArmstrong (num):
#     n = len(str(num))
#     if n == 1:
#         return True
#     if n == 2:
#         x = num%10
#         y = num//10
#         z = y % 10
#         result = x**2 + z**2
#         if result == num:
#             return True
#         else:
#             return False
#     if n == 3 :
#         x = num % 10
#         x1 = num // 10
#         y = x1 % 10
#         y1 = x1 // 10
#         z = y1 % 10
#         result = x**3 + y**3 + z**3
#         if result == num:
#             return True
#         else:
#             return False

def isArmstrong(num): # this function return true when any number is Armstrong number.
    n = len(str(num))
    result = 0
    num_cmp = num # for comparing
    for i in range(n):
        x = num%10
        num = num // 10 # here we update our number 
        result = result + x**n
    if result == num_cmp:
        return True
    else:
        return False

for i in range(1000000):
    if isArmstrong(i):
        print(i)

