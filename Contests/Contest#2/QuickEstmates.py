import sys
from collections import defaultdict

def dfs(g, n, visited):
    visited.add(n)
    for child in g[n]:
        if child not in visited:
            dfs(g, child, visited)
    return visited


h = 0
c = 0
i = 0

conn = defaultdict(list)

for line in sys.stdin:
    if i == 0:
        h, c = [int(x) for x in line.split()]
        i += 1
    else:
        h1, h2 = [int(x) for x in line.split()]
        conn[h1].append(h2)
        conn[h2].append(h1)

og_houses = set()
for i in range(h):
    og_houses.add(i+1)

ans = dfs(conn, 1, set())
if len(og_houses) < 1:
    print("")
elif len(og_houses-ans)<1:
    print("Connected")
else:
    print('\n'.join(str(x) for x in og_houses-ans))