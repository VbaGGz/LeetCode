
nums = [2,7,11,15]
target = 9

def Sum_Two(nums,target):
    numDict={}
    n=len(nums) 
    for i in range(0,n):
        sub=target-nums[i]
        if(sub in numDict):
            return [numDict[sub], i]
        numDict[nums[i]]=i

print(Sum_Two(nums,target))