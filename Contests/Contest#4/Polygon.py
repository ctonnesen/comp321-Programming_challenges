import numpy as np

external_register = -1
while external_register != 0:
    cases = int(input())
    points = []
    x_array=[]
    y_array=[]
    for case in range(cases):
        x,y = (int(x) for x in input().split())
        x_array.append(x)
        y_array.append(y)
    i = np.arange(len(x_array))
    x_array=np.array(x_array)
    y_array=np.array(y_array)
    area = np.abs(np.sum(x_array[i-1]*y_array[i]-x_array[i]*y_array[i-1])*0.5)
    direction=None
    for case in range(x_array-1):
        if x_array[case] < x_array[case+1]:
            direction="CW"
        else:
            direct = "CCW"
    print(direction)
    external_register = int(input())


