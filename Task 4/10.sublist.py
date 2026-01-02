import numbers

given_list=[4,2,-3,1,6]  #given list
n=len(given_list) # Length of the list
seen_numbers=set()  # To store prefix sums we've seen before
sum_given=0   # Running prefix sum
found=False  # to indicate if a zero-sum exists
for i in range(n):
    sum_given+=given_list[i]  # Add current element to running sum
    if sum_given==0:
        found=True
        break
    if sum_given == seen_numbers: #seen numbers is already set
        found = True
        break
    seen_numbers.add(sum_given) #Adds the current prefix to set so we can check for repeats later

    if found:
        print("Subarray with sum 0 exists") #prints the result
    else:
        print("No subarray with sum 0")

