from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    h = {}
    for i, num in enumerate(numbers):
        print(i,num)
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n]+1, i+1]

numbers = [2,7,11,15] 
target = 9

answer = twoSum(numbers,target)
print(answer)