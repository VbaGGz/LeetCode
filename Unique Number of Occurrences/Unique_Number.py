arr = [1,2,2,1,1,3]

def uniqueNumbers(nums):
    myNumberCount = {}
    for num in nums:
        if num in myNumberCount:
            myNumberCount[num] += 1
        else:
            myNumberCount[num] = 1
    if min(list(myNumberCount.values())) == 1:
        return True
    else:
        return False

print(uniqueNumbers(arr))