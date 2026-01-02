num=7896  #given number
num=str(num) # converted int to string to use index
first_num=int(num[0]) #first digit and int is used to covert str into integer
last_num=int(num[-1]) # last digit and int is used to covert str into integer
addition=int(first_num+last_num) # Added first and last num
print(f"Addition of first and last number is {addition}") # to print the value