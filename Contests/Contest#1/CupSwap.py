swaps=input()
cups=[1,0,0]
for char in swaps:
    if char=="A":
        temp=cups[1]
        cups[1]=cups[0]
        cups[0]=temp
    if char=="B":
        temp=cups[2]
        cups[2]=cups[1]
        cups[1]=temp
    if char=="C":
        temp=cups[2]
        cups[2]=cups[0]
        cups[0]=temp
for index in range(len(cups)):
    if cups[index]==1:
        print(index+1)