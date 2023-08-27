import math
import sys


def findx_power(number):
    power = 1
    root = 3
    best = 0
    while root >= 2:
        root = math.pow(number, (1 / power))
        if root == math.floor(root):
            best = power
        power += 1
    print(best)


for line in sys.stdin:
    if int(line) == 0:
        quit()
    else:
        findx_power(int(line))
