class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answers = accumulate(nums)

        return answers
