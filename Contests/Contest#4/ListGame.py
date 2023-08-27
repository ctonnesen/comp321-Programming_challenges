import math
value = int(input())


def primeFactors(n):
    final_sum=0
    while n%2==0:
        final_sum += 1
        n=n/2
    for i in range (3,int(math.sqrt(n))+1,2):
        while n%i==0:
            final_sum+=1
            n=n/i
    if n>2:
        final_sum += 1
    print(final_sum)

primeFactors(value)