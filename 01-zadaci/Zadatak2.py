def setDictionary(li:list[int] = [8,7,1], dic: dict[int, int] = {1:2, 2:1, 3:2}) :
    if(isinstance(li, list) and isinstance(dic, dict) and (len(li) == len(dic)) and all(isinstance(elem, int) for elem in li)):
        dictValues = []
        for x in li:
            if x > 10 or x < 5:
                x = -1
            else:
                x = x
            dictValues.append(x)
        newDict =  {k: v for k, v in enumerate(dictValues, 1)}
        print(newDict)        
    else:
        print('error')
        
setDictionary()