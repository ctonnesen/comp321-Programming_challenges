import math
import sys


def run_game(left, right):
    if left > right:
        return run_game(right, left)
    if right % left == 0:
        return True
    if right // left == 1:
        return not run_game(left, right - left)
    return True


for line in sys.stdin:
    if line == "0 0\n":
        break
    else:
        num1, num2 = (int(x) for x in line.split())
        if num2 > num1:
            result = run_game(num2, num1)
        else:
            result = run_game(num1, num2)
    if result:
        print("Stan wins")
    else:
        print("Ollie wins")
