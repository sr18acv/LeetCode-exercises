class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0

        for idx, ele in enumerate(nums):
            right -= ele

            if right ==left:
                return idx
            left+=ele
        return -1   
