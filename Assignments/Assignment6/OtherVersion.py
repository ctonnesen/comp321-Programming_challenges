def bird_finder(wire, distance, birds_num):
    line = [0] * wire
    for i in range(birds_num):
        bird = int(input())
        line[bird - 1] = 1
    overall_new = 0
    tracker = 0
    current = 6
    if wire <= 12:
        print("0")
        return
    if birds_num == 0:
        overall_new = (wire - 12) // distance + 1
    else:
        last_bird=7
        while current <= wire - 6:
            if line[current] == 1 or current == wire-6:
                total=0
                if tracker % (distance-1) == 0:
                    total = int((tracker / (distance-1)))
                else:
                    total = (tracker // distance) - 1
                overall_new += total
                for i in range(total):
                    line[last_bird+(i+1)*dist] = 1
                tracker = 0
                current += 1
                last_bird=current
                continue
            current += 1
            tracker += 1
    print(overall_new)
    print(line)


wire_length, dist, num_birds = [int(x) for x in input().split(" ")]
bird_finder(wire_length, dist, num_birds)
