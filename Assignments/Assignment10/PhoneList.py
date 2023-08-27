def checker(nums):
    for current in range(len(nums)-1):
            if nums[current] == nums[current+1][:len(nums[current])]:
                return "NO"
    return "YES"

testcases = int(input())
for i in range(testcases):
    rows = int(input())
    nums=[]
    for j in range(rows):
        nums.append(input())
    nums.sort()
    print(checker(nums))




