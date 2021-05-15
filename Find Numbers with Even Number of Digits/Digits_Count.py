nums = [12,345,2,6,7896]
def findNumbers(nums) -> int:
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
        else:
            continue
    return count

print(findNumbers(nums))
