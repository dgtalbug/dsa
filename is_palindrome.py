# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: sentence = "A man, a plan, a canal, Panama!"
# Output: true

# Example 2:

# Input: sentence = "race a car"
# Output: true

class PalindromeChecker:
    def is_palindrome(self, s):
        string = "".join(char.lower() for char in s if char.isalnum() )

        start, end = 0, len(string) - 1
        while start < end:
            if string[start] == string[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True
    
checker = PalindromeChecker()
sentence1 = "A man, a plan, a canal, Panama!"
sentence2 = "race a car"
print(checker.is_palindrome(sentence1))
print(checker.is_palindrome(sentence2))