import math

for tests in range(int(input())):
    position = [0,0,0]
    for directions in range(int(input())):
        command,length = input().split(" ")
        if command == "fd":
            newx, newy = (position[0]+int(length)*math.cos(position[2]), position[1] + int(length)*math.sin(position[2]))
            position = [newx, newy, position[2]]
        if command == "lt":
            newpos = (position[2]+ math.radians(int(length)))%(2*math.pi)
            position[2] = newpos
        if command == "rt":
            newpos = (position[2]- math.radians(int(length)))%(2*math.pi)
            if newpos < 0:
                newpos = (2*math.pi)+newpos
            position[2] = newpos
        if command == "bk":
            newx, newy = (position[0]-int(length)*math.cos(position[2]), position[1] - int(length)*math.sin(position[2]))
            position = [newx, newy, position[2]]
    distance = math.sqrt((0-position[0])**2+(0-position[1])**2)
    print(round(distance))