# Solution of Problem statement 2

print("\t\tWelcome To! \n \t Divide The Apple Program\n")
while(True):
    try:
        no_of_apple = int(input("Enter Number of Apple You Want to Give\n"))
        min_Student = int(input("Enter minimum no. of student\n"))
        max_Student = int(input("Enter maximum no. of student\n"))
        
        if(min_Student >= no_of_apple) :
            print("Give More Apple Then Minimum Students ")
            continue
        elif(min_Student >= max_Student):
            print("Please Enter Max greater then min")
            continue
        else:
            for i in range(min_Student,max_Student+1):
                rem = no_of_apple % i
                print(i)
                print(rem)
                if rem == 0:
                    print(f"{i} which is number between  min to max devisor of No. of apple\n")
                    print(f"Apple is Equally distributed between each student \n Each student get {no_of_apple / i}\n")
                elif rem != 0:
                    print(f"{i} which is number between  min to max is not devisor of No. of apple\n")
                    avg = no_of_apple/2
                    if (rem >= avg ):
                        request_apple = int(input(f"Please Give {no_of_apple - rem} more apple\n"))
                        no_of_apple_updated = request_apple + no_of_apple
                        print(f"Apple is Equally distributed between each student \n Each student get {no_of_apple_updated / i}\n")
                    elif(rem < avg) :
                        print(f"Hey My friend i am returning {rem} apples to you And Thank You\n")
                        no_of_apple_updated = no_of_apple - rem
                        print(f"Apple is Equally distributed between each student \n Each student get {no_of_apple_updated / i}\n")
        break
    except:
        print("Check input ,Enter Intgers Only")
        continue