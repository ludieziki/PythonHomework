# Реализуйте алгоритм перемешивания списка.

from random import choices
initialList = [2,5,6,8,3,9]

newList = choices(initialList, k=len(initialList))

#for i in initialList:
    #print(choice(initialList))
    #print(choice(initialList))
    #newList.append(initialList.pop(initialList.index(choice(initialList))))
    #newList.append(choice(initialList))

#initialList = list(set(initialList))

print(initialList)
print(newList)