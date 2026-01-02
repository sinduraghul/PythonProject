numbers_list=[4,6,7,10,13,14,17,19,20]#list of numbers
is_even=lambda num: num % 2==0 #lamba expression to check num divisible by 2
square_of_even=[num**2 for num in numbers_list if is_even(num)] # comprehensive to square the numbers divisible by 2
print(f"The square of even numbers {square_of_even}") #print the squared numbers
