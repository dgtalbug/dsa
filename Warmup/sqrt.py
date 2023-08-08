# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Example 1:

# Input: x = 8
# Output: 2

# Example 2:

# Input: x = 4
# Output: 2


class SqrtChecker:
    def find_sqrt(self, x):
        if x < 2:
             return x
        
        start, end = 2, x // 2
        midPoint = pivot = 0
        while start <= end:
            midPoint = (start + end) // 2
            pivot = midPoint * midPoint

            if pivot < x:
                start = midPoint + 1
            elif pivot > x:
                end = midPoint - 1 
            else:
                return midPoint
        return end
checker = SqrtChecker()
print(checker.find_sqrt(8))
print(checker.find_sqrt(4))