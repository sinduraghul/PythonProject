list1 = [1, 2, 20, 4, 55, 66, 7, 8, 91, 10] #list 1
list2 = [2,89,9,10,20]  #list2
list3 = [27,6,95,10,20]  #list 3
# coverts list into set
set1=set(list1)
set2=set(list2)
set3=set(list3)

duplicates= set1 & set2 & set3  # finding common in list
print(f"duplicates in the  three list {duplicates}") #print the result
