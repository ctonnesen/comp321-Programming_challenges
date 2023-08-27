def mergeSort(cur_list):
    if len(cur_list) == 1:
        return cur_list, 0
    else:
        left_list = cur_list[:len(cur_list) // 2]
        right_list = cur_list[len(cur_list) // 2:]
        left_list, rSwaps = mergeSort(left_list)
        right_list, lSwaps = mergeSort(right_list)
        temp = []
        i = 0
        j = 0
        changes = 0 + rSwaps + lSwaps
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            temp.append(left_list[i])
            i += 1
        else:
            temp.append(right_list[j])
            j += 1
            changes += (len(left_list)-i)
    temp += left_list[i:]
    temp += right_list[j:]
    return temp, changes

print(mergeSort([3,1,2,1]))