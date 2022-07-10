from typing import List

def pivotIndex(nums: List[int]) -> int:
    left = 0
    right = sum(nums)
    for i in range(len(nums)): 
        right -= nums[i]
        if left == right:
            return i
        left += nums[i] 
    return -1 

num_list = list(map(int, input().split()))

print(pivotIndex(num_list))
