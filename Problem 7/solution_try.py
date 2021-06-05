sentences = ["this is good","python is good","python is not python snake","hello how are you",
"what are you doing","facebook is good ","hello pankaj","google are" ,"harry" ,"code is",""]

a = "pankaj" # input string which is given by user
b = a.split(" ") 
relvence=0
relvence_list = []
search_result = []
for item in sentences: 
    item_split = item.split(" ")
    print(item_split)
    for i in item_split:
        for j in b:
            if ( j==i):
                relvence += 1
            else:
                pass
   
    relvence_list.append(relvence)
    relvence = 0

    
print(relvence_list)
relvence_list_1 = relvence_list[:] # it give copy of list otherwise if we assign directly list to it when we change in assigned thing our original list also change.

for item in relvence_list_1:
    max_val = max(relvence_list_1)
    if max_val == 0 :
        pass
    else:
        index_val = relvence_list_1.index(max_val)
        search_result.append(sentences[index_val])
        relvence_list_1[index_val] = 0

i = 1
for result in search_result: # this loop is for showing final result
    print(f"{i}.{result}")
    i += 1
k=0
for item in relvence_list: # If search query is not found
    if item == 0:
         k += 1
    else:
        pass

if len(relvence_list) == k :
    print("Sorry Your Result is not found")
