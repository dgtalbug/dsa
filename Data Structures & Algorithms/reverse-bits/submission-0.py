class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        
        return res

        # inp = str(n)

        # left = 0
        # right = len(inp) -1

        # reversed_bits = list(inp)

        # while left <= right:

        #     reversed_bits[left], reversed_bits[right] = reversed_bits[right], reversed_bits[left]
        #     left += 1
        #     right -= 1    
        
        # reversed_bin_str = ''.join(reversed_bits)
        # return int(reversed_bin_str, 2)