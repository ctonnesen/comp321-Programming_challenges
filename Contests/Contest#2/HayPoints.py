letters = [int(x) for x in input().split(" ")]
example_dict = {}
for i in range(letters[0]):
    words, price = [x for x in input().split(" ")]
    example_dict[words] = int(price)
for j in range(letters[1]):
    hit_end= False
    current_list=[]
    while True:
        line = input()
        broken = [x for x in line.split(" ")]
        if input == ".":
            hit_end=True
            break
        current_list.extend(broken)
    if hit_end:
        continue
    mysum = 0
    for word in current_list:2
        if word in example_dict.keys():
            mysum += example_dict.get(word)

    print(mysum)