def first_non_repeating(lst):  # defined a function

    occurences={} # count the occurences
    for num in lst:
        if num in occurences:
            occurences[num] += 1  # used to increase number count
        else:
              occurences[num] = 1
        print (occurences)  #print the occurences
    for num in lst:
        if occurences[num] == 1:  #to find first non repeating integer count
         return num
    return None
numbers=[4,5,1,5,9,3,4,5,1,8,6,3]  # numbers given
print(first_non_repeating (numbers)) #prints the number




