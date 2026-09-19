class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            print(res, res + (i -nums[i]))
            res += i - nums[i]
         
        return res

