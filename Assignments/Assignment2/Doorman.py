def doorman(limit, line):
    if limit == 0 or line == 0:
        return 0
    char = line[0]
    line = line[1:]
    mapping = {"M": 0, "W": 0}
    mapping[char] = mapping[char] + 1
    count = 1
    swap = False
    i = 0
    while i < len(line):
        mapping[line[i]] = mapping[line[i]] + 1
        if limit < abs(mapping["M"] - mapping["W"]):
            if swap:
                return count
            else:
                mapping[line[i]] = mapping[line[i]] - 1
                t = list(line)
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = temp
                line = ''.join(t)
                swap = True
                continue
        swap = False
        count = count + 1
        i = i + 1
    return count


limit = int(input())
line = input()
print(doorman(limit, line))
