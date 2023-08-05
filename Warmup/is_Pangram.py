# Given a string sentence containing English letters (lower- or upper-case), return true if sentence is a Pangram, or false otherwise.

# A Pangram is a sentence where every letter of the English alphabet appears at least once.

# Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

# Example 1:

# Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
# Output: true

# Example 2:

# Input: sentence = "This is not a pangram"
# Output: false


class PangramChecker:
    def is_pangram(self, sentence):

        if len(sentence) < 26:
            return False
        
        sentence = sentence.lower()  # convert to lower case
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char not in sentence:
                return False  # If a character is not found, it's not a pangram
        return True  # If all characters are found, it's a pangram
    


sentences = [
    "TheQuickBrownFoxJumpsOverTheLazyDog",
    "This is not a pangram",
    # add more sentences here...
]

check = PangramChecker()
for i, sentence in enumerate(sentences, 1):
        print(f"Sentence{i} is pangram? {check.is_pangram(sentence)}")