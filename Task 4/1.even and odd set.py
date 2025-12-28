numbers=[10, 501, 22, 37, 100, 999, 87, 351]  # input list
even_numbers=[] #empty list to store result of even
odd_numbers=[]  #empty list to store result of odd

for num in numbers: #loop for num_list
    if num % 2 == 0:  #checks number divisible by 2 true (even) false (odd)
        even_numbers.append(num) # append adds current numbers at end of list
    else:
        odd_numbers.append(num)
# prints the result
print(f"Even numbers {even_numbers}")
print(f"Odd numbers {odd_numbers}")