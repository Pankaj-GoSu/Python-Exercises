# Solution of Problem statement 4

# ========= First writing program for palindrome (To detect any no. is palindrome or not).===========

# inp =  input("Enter number one by one after giving space") # taking input from user 
# inp_= inp.split(" ") # here we split and make one list inp_
# print(inp_)
# def palindrome_func(User_list):
#     global result
#     i=0 # initializing i for loop
#     while(i<len(User_list)):
#         if (User_list[i] == User_list[len(User_list)-i-1]) : # main logic here we compare strings
#             i=i+1
#             pass
#         else:
#             print("This is not a palindrome")
#             break

#     if i==len(User_list): # This logic is important for print number is palindrome or not .
#         result = "This is a palindrome"
# result = result

# ========================= Solution ======================

print("\t\t Welcome To ! \n \t The Next Palindrome Program")

test_inp = int(input("Enter how many numberes you want to enter for getting Next palindrome")) # Taking test input from user
inp_list = []
for i in range(test_inp):
    inp_list.append(input("Enter The Number you want to find the Next Palindrome"))

for lists in inp_list:
    if lists == lists[::-1]:
        print(f"{lists} is already a palindrome ")
    else:
        lists_int = int(lists)
        while(True):
            lists_int = lists_int + 1
            lists_str = str(lists_int)
            if lists_str == lists_str[::-1]:
                print(f"{lists_str} is Your Next Palindrome")
                break
            else:
                continue

