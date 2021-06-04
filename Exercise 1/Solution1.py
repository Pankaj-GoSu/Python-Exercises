# Solution For Problem statement 1

def age_cal():
    while(True):
        try:
            age_or_year = input("Enter Your age or year of birth \n")
            len_age = int(len(age_or_year)) # to calculate length of given input
            age_or_year = int(age_or_year)
    
            if (len_age <= 3):
                if (age_or_year<=0):
                    print("You are not yet born")
                elif(130>age_or_year>100):
                    print(f"You already cross 100 and your age is {age_or_year-100} year more then")
                elif(160>age_or_year>=130):
                    print("You seem to be oldest person alive")
                elif(age_or_year>160):
                    print("This Is Not possible Please check your Input")
                elif(age_or_year==100):
                    print("You are now 100 year old")
                else:
                    age_rem = 100 - age_or_year # To calculate when he will turns 100
                    print(f"After {age_rem} You will becomes 100 year old")
            elif (len_age == 4):
                if(age_or_year >= 2022): #assuming present year is 2021
                    print("You are not yet born")
                elif(1900<=age_or_year<1920):
                    print("You already cross 100")
                elif(1860<=age_or_year<1900):
                    print("You seem to be oldest person alive")
                elif(age_or_year<1860):
                    print("This Is Not possible Please check your Input")
                else:
                    present_age = 2021 - age_or_year
                    age_rem = 100 - present_age
                    print(f"In year {2021+age_rem} You become 100 year old" )
            else:
                print("Please Check Your Input Only Give Your age or Year of birth")
                continue
            break        
        except:
            print("Please Check Your Input Only Give Your age or Year of birth")
            continue
print("\t\t \t Welcome ! \n \t  Here You know when you are turn to 100")
age_cal()
while(True):
    inp = input("You want to know your age [y/n]")
    if (inp == "y"):
        year = int(input("Enter Your year of birth \n"))
        if (year<1860):
            print("According To our System it is not possible")
        elif(year>2021):
            print("According To our System you are not yet born")
        else:
            print(f"You are now {2021-year} old")
    elif(inp == "n"):
        exit()
    else:
        print("Please check your input and give input again")
        continue