# Solution of Problem statement 4


# ========================= Solution ======================

print("\t\t Welcome To ! \n \t The Next Palindrome Program")
while(True):
    try:
        test_inp = int(input("Enter how many numberes you want to enter for getting Next palindrome\n")) # Taking test input from user
        inp_list = [] # blank list for store no. of inputs given by user
        for i in range(test_inp): # for loop for store inputs in list
            inp_list.append(input("Enter The Number you want to find the Next Palindrome\n"))

        for lists in inp_list: # this loop for iterate inputs one bye one .
            if lists == lists[::-1]: #checking given input is palindrome or not
                print(f"{lists} is already a palindrome \n")
            else:
                lists_int = int(lists)
                while(True):
                    lists_int = lists_int + 1
                    lists_str = str(lists_int)
                    if lists_str == lists_str[::-1]: # for checking palindrome in string
                        print(f"Next palindrome for {lists} is {lists_str}.\n")
                        break
                    else:
                        continue
        # below line added for looping if you eant to reuse this system
        inp = input("You want to check again for diffrent no. \n press y for continue or press any key to exit()\n")
        if (inp=="y"):
            continue
        else:
            break
    except:
        # below line added for looping , even after wrong input you can use again
        print("Please Enter Integer values You want to continue press [y] for exit press any key\n")
        if (input() == "y"):
            continue
        else:
            break
