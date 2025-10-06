def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [10,20,30,40,50]

pos1, pos2 = 2,4
print(swapPositions(list, pos1-1, pos2-1))