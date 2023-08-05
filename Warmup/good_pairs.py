# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4

# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6

class PairChecker:
    def good_Pairs(self, nums):
        left = right = 0
        pairsFound = 0
        
        for i in range(len(nums)):
            left = i
            right = i + 1
            while left < len(nums) and right < len(nums):
                if nums[left] == nums[right]:
                    pairsFound += 1
                    left = right
                right += 1
        return pairsFound

checker = PairChecker()
nums = [1,1,1,1]
print(checker.good_Pairs(nums))
