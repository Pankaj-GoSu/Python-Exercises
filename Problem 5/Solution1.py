# ============= Solution of Problem statement 2 ===================

print("\t\t Welcome To ! \n\t Palindromify The List")
len_lst = int(input("Please Enter Length of List:\n"))
lst = []
list_out = []

for i in range(len_lst):
    lst.append(int(input("Give Input one by one:\n")))
# lst = [1, 6, 87, 43]  # Taking list

for item in lst:  # for iterate 'lst' list.

    if item < 10:
        list_out.append(item)
    else:
        item = str(item)  # typecaste into str for palindrome checking
        if item == item[::-1]:  # palindrome check
            list_out.append(int(item))

        else:
            item = int(item)
            while True:  # This loop for making a number into next palindrome no.
                item += 1
                item_new = str(item)
                if item_new == item_new[::-1]:
                    list_out.append(int(item_new))
                    break
                else:
                    continue

print(f" Your list {lst} Palindrome into {list_out}")
