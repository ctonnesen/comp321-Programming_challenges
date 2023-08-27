testcases = int(input())
for testcase in range(testcases):
    number = int(input())
    if abs(number) % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
