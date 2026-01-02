numbers = [10, 20, 30, 9]  # the list of numbers
value = 59  # target sum
n=len(numbers)  # length of the list (here n = 4)
triplets=[]   # empty list to  store triplet value

# Three nested loops to pick all possible triplets
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
          if numbers[i] + numbers[j] + numbers[k] == value:
              triplets.append((numbers[i], numbers[j], numbers[k]))
              print("triplet number", triplets) #print triplet number



