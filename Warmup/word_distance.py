# Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

# Example 1:

# Input: words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
# Output: 5

# Example 2:

# Input: words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"
# Output: 1


class DistanceChecker:
    def find_Distance(self, words, start, end):
        pos1 = pos2 =  -1
        shortDistance = len(words)
        for i in range(len(words)):
            if words[i] == start:
                pos1 = i
            elif words[i] == end:
                pos2 = i
        
            if pos1 != -1 and pos2 != -1:
                shortDistance = min(shortDistance, abs(pos1 - pos2))


        return shortDistance


checker = DistanceChecker()
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
start = "fox"
end = "dog"
print(checker.find_Distance(words, start, end))
words = ["a", "c", "d", "b", "a"]
start = "a"
end = "b"
print(checker.find_Distance(words, start, end))
words = ["repeated", "words", "in", "the", "array", "words"]
start = "repeated"
end = "words"
print(checker.find_Distance(words, start, end))