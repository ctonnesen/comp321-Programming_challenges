import math
d,s = [int(x) for x in input().split()]
outer_a = None
a=1
while outer_a is None:
    left = a*s
    right = a*math.cosh(d/(2*a))
    if left == right:
        outer_a = a
    a+=1
print(2*outer_a*math.sinh(d/(2*outer_a)))
