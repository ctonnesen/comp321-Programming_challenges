train = input()
capacity = int(train.split(" ")[0])
stops = int(train.split(" ")[1])
onboard=0
for n in range(stops):
    left, enter, station_remain = input().split(" ")
    onboard -= int(left)
    if onboard < 0:
        print("impossible")
        quit()
    onboard += int(enter)
    if onboard > capacity:
        print("impossible")
        quit()
    difference = capacity-onboard
    if int(station_remain) < difference:
        print("impossible")
        quit()
print("possible")