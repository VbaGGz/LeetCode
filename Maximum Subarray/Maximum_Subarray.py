from typing import List
def maxSubArray(nums: List[int]) -> int:
    size = len(nums)
    maxSum = nums[0]
    prevSum = nums[0]
    for i in range(1,size):
        prevSum = max(prevSum + nums[i],nums[i])
        maxSum = max(prevSum,maxSum)
    return maxSum