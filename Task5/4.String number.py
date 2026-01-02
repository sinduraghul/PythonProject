is_number = lambda s: s.isdigit() #lamba function to check string is a number
test_strings=["456","789","4.5","abc"] #strings given
for s in test_strings: #for loop to check given string is number
    print(f"The string {s} is: {is_number(s)}") # Print the string true or false

