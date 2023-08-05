# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "cinema", t = "iceman"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class AnagramChecker:
    def is_Anagram(self, source, toCheck):
        # If the lengths of the two strings are not the same, 
        # they can't be anagrams of each other, so return False
        if len(source) != len(toCheck):
            return False
        
        count_s = dict()
        count_t = dict()

         # Count the occurrence of each character in s
        for char in source:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        # Count the occurrence of each character in t
        for char in toCheck:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        # If the count dictionaries are the same, s and t are anagrams of each other
        return count_s == count_t

checker = AnagramChecker()

# Test inputs
print(f"'cinema', 'iceman' are anagrams? {checker.is_Anagram('cinema', 'iceman')}")  # Should return True
print(f"'rat', 'car' are anagrams? {checker.is_Anagram('rat', 'car')}")  # Should return False

