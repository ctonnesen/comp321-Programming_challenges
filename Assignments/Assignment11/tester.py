#include <algorithm>
#include <iostream>
#include <vector>
import sys

def play(a, b) :


    if(b % a == 0) :
        return True;


    if((b/a) == 1) :
        return not play(a, b-a);

    return True;


for line in sys.stdin:
    if line == "0 0\n":
        break
    else:
        a, b = (int(x) for x in line.split())
        if(b > a):
            temp = a
            a = b
            b = temp

        winner = play(a, b);
        if(winner):
            print("stan");

        else:
            print("Ollie");
