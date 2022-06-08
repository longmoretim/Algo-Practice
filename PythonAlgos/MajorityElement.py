def majorityElem(arr):
    #reduce array to unique elements
    #count number of occurences in original Arr and keep track of most
    tempArr = []
    for x in arr:
        if tempArr.count(x) == 0:
            tempArr.append(x)

    highNum = 0

    for j in tempArr:
        if arr.count(j) > arr.count(highNum):
            highNum = j
    return highNum

print(majorityElem([2,2,1,1,1,2,2]))