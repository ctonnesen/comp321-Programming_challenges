import sys

target = (1,1)
invalid = set()
curr_row = 0
k = (-1 , -1)
i = 0
for line in sys.stdin:
    if i==0:
        i+=1
        continue
    cells = [x for x in line if x != '\n']
    for col,c in enumerate(cells):
        if c == 'K':
            k = (curr_row,col)
        if c == '#':
            invalid.add((curr_row,col))
    curr_row += 1

print("invalids:",invalid)
print("k:",k)

def compute_moves(square):
    r_perms = [2,2,-2,-2,1,1,-1,-1]
    c_perms = []