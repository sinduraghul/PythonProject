a = [10, 501, 22, 37, 100, 999, 87, 351] #list of happy num want to check
b = [] # Empty list to store happy numbers
def happy(a):   # define fun to check which numbers in list 'a' are happy num
    for i in range (len(a)): #loops through each number in the list a
        n = a[i]  #takes current number
        while n!=1 and n !=4:
            tempsum = 0  # start with 0 before adding anything
            for digit in str(n): # convert the number into a string E
                                 # Eg:- if n = 22, then str(n) → "82" → digits "2" and "2".
                tempsum += int(digit) ** 2 #- square each digit and add it to tempsum
            n = tempsum  # replaces old number with new num in loop
        if n == 1:
            b.append(a[i])
    return b #happy numbers stored
print(happy(a)) #happy numbers printed

# while n!=1 and n !=4:
#  the loop will continue to execute as long as the
# value of the variable n is not equal to 1 and is also not equal to 4
# The loop terminates immediately when n becomes either 1 or 4
