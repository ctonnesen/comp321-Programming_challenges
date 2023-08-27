points, interval = [int(x) for x in input().split()]
point_list = []
previous = (0,0,0)
first = False
last_pos = None
for point in range(points):
    if first == False:
        x,y,t = [int(x) for x in input().split()]
        previous = (x,y,t)
        first = True
    x, y, t = [int(x) for x in input().split()]
    dist =

