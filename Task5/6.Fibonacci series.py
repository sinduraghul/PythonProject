from functools import reduce #import reduce function

#function applied
#range(n-2) - iteration is applied
#[0,1]- initialize the value
fib_series = lambda n: reduce(lambda x, _: x + [x[-1]] + [x[-2]],range(n-2),[0,1])
#n series given
print(f"Fibonacci series upto 2:{fib_series(2)}")
print(f"Fibonacci series upto 5:{fib_series(5)}")


