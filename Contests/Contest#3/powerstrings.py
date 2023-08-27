from collections import defaultdict
from math import inf
s = input()
while s != '.':
    g = defaultdict(int)
    for c in s:
        g[c] += 1
    # print(g)
    least = inf
    for n in g:
        least = min(least,g[n])
    print(least)
    s = input()

