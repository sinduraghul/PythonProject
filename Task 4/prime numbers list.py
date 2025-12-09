num_list =[10,501,22,37,100,999,87,351]
prime_numbers=[]
for i in num_list:
    c=0
    for j in range(1,i):
        if i%j == 0:
            c += 1
    if c == 1:
      prime_numbers.append(i)
print(f"Prime number:{prime_numbers}")
print(f"count the prime numbers:{len(prime_numbers)}")




