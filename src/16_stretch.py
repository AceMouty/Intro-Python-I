import math

print("Enter the a number")
number = int(input())

primes = [i for i in range(2, number + 1)]

i = 2
# from 2 to sqrt(number)
while(i <= int(math.sqrt(number))):
    print(f"Ths sqrt of {number} is {int(math.sqrt(number))}")
    # if i is in list
    # then we gotta delete its multiples
    if i in primes:
        # j will give multiples of i,
        # starting from 2*i
        for j in range(i*2, number+1, i):
            print(j)
            if j in primes:
                # deleting the multiple if found in list
                primes.remove(j)
    i = i+1

print(primes)
