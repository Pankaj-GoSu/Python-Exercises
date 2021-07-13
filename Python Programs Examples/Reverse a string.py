#======== Reverse a String Using for loop ========

result = ""

string = "Pankaj"
# ===>> To Reverse a string.
for i in range(len(string)-1,-1,-1):
    result = result + string[i]

print(result)