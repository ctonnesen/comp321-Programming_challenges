n = int(input())

# total = 0
base = 2
while n > 0:
    n -= 1
    base = ((base*2)-1)
total = base**2
print(total)
