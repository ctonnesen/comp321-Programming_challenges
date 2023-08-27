cases = int(input())
for i in range(cases):
    current = input()
    length = 0
    for char_index in range(0, len(current)+1):
        length += 1
        plusone = char_index+1
        np = current[:plusone]
        comp = current[plusone:plusone+length]
        comp1 = current[plusone+length:plusone + 2*length]
        if np == comp and plusone + 2*length > len(current):
            print(char_index+1)
            break
