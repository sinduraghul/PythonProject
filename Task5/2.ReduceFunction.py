from functools import reduce #import
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #numbers list
products=reduce(lambda x, y: x * y, numbers) #reduce lambda function to calculate(product) numbers
print(f"The list of numbers {numbers}") #print numbers list
print(f"The product of numbers {products}") #print the product numbers
