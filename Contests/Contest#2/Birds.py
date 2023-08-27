from math import floor

length, dist, num_birds = [int(x) for x in input().split(" ")]
line = [0]*length
for i in range(num_birds):
    bird = int(input())
    line[bird-1]=1
overall_new=0
tracker = 0
current = 6
while current <= length-5:
    if line[current]==1 or current == length-6:
        overall_new += floor(tracker/dist)
        tracker = 0
        current += 1
        continue;
    tracker+=1
    current+=1
# if num_birds == 0:
#     overall_new+= 2
print(overall_new)