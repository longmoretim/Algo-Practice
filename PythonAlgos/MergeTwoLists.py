#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

def mergeTwo(one, two):
    three = one + two
    three.sort()
    return three

print(mergeTwo([1,2,8], [4,5,6,7]))