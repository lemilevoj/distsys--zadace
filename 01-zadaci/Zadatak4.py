list1 = [1,2,3,4,5]
list2 = [2,2,4,4,5]
newList = []
def returnList(list1, list2): 
    for pos,value in enumerate(list1):
        newList.append(value if value == list2[pos] else -1 )
    return newList
