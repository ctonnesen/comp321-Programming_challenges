t_coords = []
for i in range(3):
    x,y = input().split(" ")
    t_coords.append((int(x), int(y)))
land_owned = abs(t_coords[0][0]*(t_coords[1][1]-t_coords[2][1])+t_coords[1][0]*(t_coords[2][1]-t_coords[0][1])+t_coords[2][0]*(t_coords[0][1]-t_coords[1][1]))/2
trees_in=0
for i in range(int(input())):
    x, y = input().split(" ")
    point = (int(x), int(y))
    #swap A's
    area1 = abs(point[0]*(t_coords[1][1]-t_coords[2][1])+t_coords[1][0]*(t_coords[2][1]-point[1])+t_coords[2][0]*(point[1]-t_coords[1][1]))/2
    #swap B's
    area2 = abs(t_coords[0][0]*(point[1]-t_coords[2][1])+point[0]*(t_coords[2][1]-t_coords[0][1])+t_coords[2][0]*(t_coords[0][1]-point[1]))/2
    #swap C's
    area3 = abs(t_coords[0][0]*(t_coords[1][1]-point[1])+t_coords[1][0]*(point[1]-t_coords[0][1])+point[0]*(t_coords[0][1]-t_coords[1][1]))/2
    if area1+area2+area3==land_owned:
        trees_in+=1
print(str(round(land_owned, 2)))
print(trees_in)



