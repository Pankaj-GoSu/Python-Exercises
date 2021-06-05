# ============= Solution of Problem statement 7 ===================

"""
Author: Pankaj(GoSu)
Date: 6 june 2021
Purpose: Practice problem

"""

# =========== My First Search Engine ===========
import time 

sentences = ["this is good","python is good","python is not python snake","hello how are you",
"what are you doing","facebook is good ","hello pankaj","google are" ,"harry" ,"code is","hi"]

query = input("Enter what you want to search\n")
time1 = time.time() # time.time() gives us a time from where it started like 3253443 sec somthing
query = query.lower()

query_split = query.split(" ") 
relvence=0
relvence_list = []
search_result = []
for item in sentences: # This loop give us how many time our query occure in each item of sentences
    item_split = item.split(" ")
    print(item_split)
    for i in item_split:
        for j in query_split :
            if ( j==i):
                relvence += 1
            else:
                pass
   
    relvence_list.append(relvence)
    relvence = 0

    
# print(relvence_list) # For testing

relvence_list_1 = relvence_list[:] # it give copy of list otherwise if we assign directly list to it when we change in assigned list thing our original list also change.

for item in relvence_list_1:
    max_val = max(relvence_list_1)
    if max_val == 0 :
        pass
    else:
        index_val = relvence_list_1.index(max_val)
        search_result.append(sentences[index_val])
        relvence_list_1[index_val] = 0

i = 1
print(f"We found Total {len(search_result)} Result for you in {time.time() - time1} sec\n")

for result in search_result: # this loop is for showing final result
    print(f"{i}.{result}\n")
    i += 1
k=0
for item in relvence_list: # If search query is not found
    if item == 0:
         k += 1
    else:
        pass

if len(relvence_list) == k :
    print("Sorry Your Result is not found\n")
