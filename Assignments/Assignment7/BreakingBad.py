from collections import defaultdict


def item_splitter():
    walter_list = set()
    jesse_list = set()
    for item in connect_dict:
        if (connect_dict[item] & walter_list) and not (connect_dict[item] & jesse_list):
            jesse_list.add(item)
            continue
        if (connect_dict[item] & jesse_list) and not (connect_dict[item] & walter_list):
            walter_list.add(item)
            continue
        if (connect_dict[item] & jesse_list) and (connect_dict[item] & walter_list):
            print("impossible")
            return
        if len(walter_list) > len(jesse_list):
            jesse_list.add(item)
        if len(walter_list) >= len(jesse_list):
            walter_list.add(item)
    remains = items - jesse_list
    walter_list.update(remains)
    print(' '.join(walter_list) + "\n" + ' '.join(jesse_list))


def new_item_splitter():
    pseudo_stack = []
    combo_list = [set(), set()]
    for item in connect_dict:
        if item in combo_list[0] or item in combo_list[1]:
            continue
        pseudo_stack.append((len(combo_list[1]) > len(combo_list[0]), item))
        while pseudo_stack:
            owner, current_item = pseudo_stack.pop()
            if current_item in combo_list[not owner]:
                print("impossible")
                quit()
            if current_item in combo_list[owner]:
                continue
            combo_list[owner].add(current_item)
            for connection in connect_dict[current_item]:
                pseudo_stack.append((not owner, connection))
    remains = items - combo_list[1]
    combo_list[0].update(remains)
    print(' '.join(combo_list[0]) + "\n" + ' '.join(combo_list[1]))
    return


num_items = int(input())
items = set()
for i in range(num_items):
    items.add(input().strip())
connections = int(input())
connect_dict = defaultdict(set)
for i in range(connections):
    item1, item2 = [x for x in input().split(" ")]
    connect_dict[item1].add(item2)
    connect_dict[item2].add(item1)
new_item_splitter()
