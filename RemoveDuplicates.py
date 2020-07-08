"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

def removeDuplicates(inputList):
    resultSet = set(inputList)
    resultList = list(resultSet)
    return resultList

def findDuplicates(inputList1, inputList2):
    resultSet = set([a for a in inputList1 if a in inputList2])
    return list(resultSet)

inputList = [1, 2, 3,2,5, 6, 1, 2, 4, 5, 2, 2]
print(removeDuplicates(inputList))

inputList2 = [1,2,4,3,4]
print(findDuplicates(inputList,inputList2))
