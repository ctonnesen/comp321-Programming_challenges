from itertools import combinations
from math import factorial


def summarizer(numbers):
    overall = 0
    for indice in range(4):
        comb = list(combinations(numbers, indice))
        for combo in comb:
            total = sum(combo)
            if total >= 200:
                overall += total
    for indice in range(4, len(numbers) + 1):
        in_sets = (factorial(len(numbers) - 1)) // (
                (factorial(indice - 1)) * (factorial(len(numbers) - 1 - (indice - 1))))
        for fruit in numbers:
            overall += in_sets * fruit
    print(overall)


# Print the obtained permutations

amount = input()
what = [False] * 2
numbers = list(map(int, input().split(" ", int(amount))))
summarizer(numbers)
