import sys
from collections import defaultdict
i = 0
g = defaultdict(list)
n,m,a,b = 0,0,0,0

visited = set()
def dfs_rec(visited,g,n):
    if n not in visited:
        print(n)
        visited.add(n)
        for neighbour in g[n]:
            dfs_rec(visited,g,n)

for i in range(n):
    g[i] = []

for line in sys.stdin:
    if i==0:
        n,m = [int(x) for x in line.split()]
        i+=1
    else:
        a,b = [int(x) for x in line.split()]
        g[b].append(a)
        # g[b].append(a)

print(g)
least = []
for n in g:
    neighbours = g[n]
    if not neighbours:
        least.append(n)

if not least:
    print("IMPOSSIBLE")
else:
    dfs_rec(visited,g,least[0])

