from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        ptr2 = len(nums) - 1
        ptr3 = 0
        
        while ptr3 <= ptr2:
            if nums[ptr3] == 0:
                nums[ptr1], nums[ptr3] = nums[ptr3], nums[ptr1]
                ptr1 += 1
                ptr3 += 1
            elif nums[ptr3] == 1:
                ptr3 += 1
            else:
                nums[ptr2], nums[ptr3] = nums[ptr3], nums[ptr2]
                ptr2 -= 1
