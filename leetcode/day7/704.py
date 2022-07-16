from typing import List


def search(nums:List[int], target:int) -> int:
    center = int(len(nums) / 2) - 1 if len(nums) > 2 else 0

    add_num = 1 if nums[center] < target else -1

    while nums[center] != target:
        if center == -1 or center == len(nums) - 1:
            center = -1
            break
        center = center + add_num
    return center
        



print(search([-1 , 0, 5], 8))