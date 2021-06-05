# Solution of Problem statement 3

print("\t\t Welcome To! \n Reversing Your list program")
while(True):
    try:
        list_inp = input("Enter Calories and put , between 2 Calories") # Taking list as input from user`
        list_calories = list_inp.split(",") # split function give us list after removing ,
        list_calories.sort() # inbuild function for short if not shorted

        reverse1 = list_calories[:] # here we give copy of list into reverse 1
        reverse1.reverse() # inbuild function for reversing list
        print(f"Given list is {list_calories} and reversed list using 1st method is {reverse1}\n")
        reverse2 = list_calories[::-1] # Reversing list using sclicing.
        print(f"Given list is {list_calories} and reversed list using 2nd method is {reverse2}\n")
        # # a=[]
        reverse3 = list_calories[:] # copy of list given to reverse3
        for i in range(len(reverse3)//2):
            reverse3[i],reverse3[len(reverse3)-i-1] = reverse3[len(reverse3)-i-1],reverse3[i]   
            # a.append(list_calories3[len_list_inp-index-1]) #We Can also use thise method for reversing out list
        print(f"Given list is {list_calories} and reversed list using 3rd method is {reverse3}\n")
        if (reverse1==reverse2 and reverse2 == reverse3): 
            print("You are able to see this print statement means all three reverse method give same result\n")
        # Below statment for looping our system 
        print("Want to give list again press[y] or press any key to exit()")
        if (input()=="y"):
            continue
        else:
            break
        
    except:
        print("Please check your input") # Error handeling using try except 
        continue