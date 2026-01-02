num_list =[10,501,22,37,100,999,87,351]  # input list
prime_numbers=[]  #empty list to store result
for i in num_list:  # Loop for num_list
    c=0             #counter to track
    for j in range(1,i):  # Check divisibility from 1 up to i-1
       if i%j == 0:  # If i is divisible by j
            c += 1   # Increase divisor count
    if c == 1:   #Prime numbers has only 1 divisor
      prime_numbers.append(i) # append adds current numbers at end of list

print(f"Prime number:{prime_numbers}") # Print Print Numbers
print(f"count the prime numbers:{len(prime_numbers)}") #print Count of prime numbers




