# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums= [1, 2, 3, 4]
# Output: false  

# Example 2:

# Input: nums= [1, 2, 3, 1]
# Output: true  

class DuplicateFinder:
    def has_duplicate(self, nums):
        counter = {}  # Dictionary to keep track of the occurrences of each number

        for num in nums:
            if num in counter:
                return True # If the number is already in the dictionary, it's a duplicate
            else:
                counter[num] = 1  # Add the number to the dictionary
        
        return False  # No duplicates found if the loop completes without returning True

# Input
check = DuplicateFinder()
nums_list = [
    [1, 2, 3, 4],
    [1, 2, 3, 1],
    # add more nums here...
]

for i, nums in enumerate(nums_list, 1):
        print(f"List{i} has duplicates? {check.has_duplicate(nums)}")


