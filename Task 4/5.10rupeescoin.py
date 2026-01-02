coins = [1, 2, 5, 10] #given coins
target = 10

solution = []  #empty list to store result

# for loop search through all possibilities
for c1 in range(target // 1 + 1):       # Rs. 1 coins
    for c2 in range(target // 2 + 1):   # Rs. 2 coins
        for c5 in range(target // 5 + 1): # Rs. 5 coins
            for c10 in range(target // 10 + 1): # Rs. 10 coins
                if c1*1 + c2*2 + c5*5 + c10*10 == target: #target to get 10 3*1+2*2+1*5+10*0+=10                    solutions.append((c1, c2, c5, c10))
                    solution.append((c1, c2, c5, c10))
# Print results
print("Ways to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5, Rs. 10 coins:")
for sol in solution:
    print(f"1-rupee:{sol[0]}, 2-rupee:{sol[1]}, 5-rupee:{sol[2]}, 10-rupee:{sol[3]}")
print(f"\nTotal ways: {len(solution)}")