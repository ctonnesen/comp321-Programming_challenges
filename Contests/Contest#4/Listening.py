x_loc, y_loc, listening = [int(x) for x in input().split()]
devices = []
for location in listening:
    x_listen, y_listen, radius = [int(x) for x in input().split()]
    devices.append((x_listen,y_listen,radius))
    