def orderDecoder(largest):
    memory = [[0 for item in prices] for price in range(largest + 1)]
    for possible_total in range(len(memory)):
        possible_items = [item for item in prices if possible_total >= item]
        for item in possible_items:
            if memory[possible_total - item] == "Ambiguous":
                memory[possible_total] = "Ambiguous"
            elif memory[possible_total - item] != memory[0]:
                fill_price_combo_list(memory, item, possible_total)
            elif possible_total == item:
                if memory[possible_total] != memory[0]:
                    memory[possible_total] = "Ambiguous"
                else:
                    memory[possible_total][prices.index(item)] += 1
    return memory


def fill_price_combo_list(memory, item, possible_total):
    copy_sublist = [i for i in (memory[possible_total - item])]
    copy_sublist[prices.index(item)] += 1
    if memory[possible_total] != memory[0] and copy_sublist != memory[possible_total]:
        memory[possible_total] = "Ambiguous"
    else:
        memory[possible_total] = [i for i in memory[possible_total - item]]
        memory[possible_total][prices.index(item)] += 1
    return


empty_combos = set()
menu_items = int(input())
menu = input()
prices = list(map(int, menu.split(" ")))
order_num = int(input())
orders = list(map(int, input().split(" ")))
memory=orderDecoder(max(orders))
for order in orders:
    if memory[order] == memory[0]:
        print("Impossible")
        continue
    if memory[order] == "Ambiguous":
        print("Ambiguous")
        continue
    else:
        combo_string = ''
        for index, item in enumerate(memory[order]):
            combo_string += (str(index+1) + ' ') * item
        print(combo_string.rstrip())