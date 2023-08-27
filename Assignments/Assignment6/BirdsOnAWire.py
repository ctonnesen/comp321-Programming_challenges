
def bird_finder(wire, distance, birds_num):
    line = []
    test_line=[0]*wire
    for i in range(birds_num):
        bird = int(input())
        line.append(bird)
        test_line[bird-1]=1
    line = sorted(line)
    overall_new = 0
    current = 6
    if birds_num == 0:
        overall_new = (wire - 12) // distance + 1
    else:
        for bird in line:
            while current + distance <= bird:
                overall_new += 1
                test_line[current]=1
                current += distance
            current = bird + distance
        while current <= (wire - 6):
            test_line[current]=1
            overall_new += 1
            current += distance
    print(overall_new)
    # print(test_line)


wire_length, dist, num_birds = [int(x) for x in input().split(" ")]
bird_finder(wire_length, dist, num_birds)
