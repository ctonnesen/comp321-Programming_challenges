def solitaire(line):
    final_count = 0
    for char in line:
        if char == 'o':
            final_count += 1
    for i in range(len(line)):
        if i < len(line) - 2:
            if line[i] == "o" and line[i + 1] == "o" and line[i + 2] == "-":
                alter = line[:i] + "--o" + line[i + 3:]
                return_value = solitaire(alter)
                if return_value < final_count:
                    final_count = return_value
        if 1 < i:
            if line[i] == "o" and line[i - 1] == "o" and line[i - 2] == "-":
                alter = line[:i - 2] + "o--" + line[i + 1:]
                return_value = solitaire(alter)
                if return_value < final_count:
                    final_count = return_value
    return final_count


testcase = int(input())
for i in range(testcase):
    line = input()
    print(solitaire(line))
