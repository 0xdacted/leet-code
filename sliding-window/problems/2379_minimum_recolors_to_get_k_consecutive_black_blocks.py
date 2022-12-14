# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. 
# The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

class Solution:
        
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minRecolors = float("inf")
        for i in range(len(blocks) + 1 - k):
            recolors = 0
            string = blocks[i:i + k]
            for c in range(k):
                if string[c] == 'W':
                    recolors += 1
            minRecolors = min(minRecolors, recolors)

        return minRecolors


class Solution:
        
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minRecolors = k
        length = len(blocks) - k + 1
        for i in range(length):
            sub = blocks[i:i+k]
            recolors = sub.count('W')
            minRecolors = min(minRecolors, recolors)
        return minRecolors

class Solution:
        
    def minimumRecolors(self, blocks: str, k: int) -> int:
        recolors = 0
        for i in range(k):
            if blocks[i] == 'W':
                recolors += 1
        minRecolors = recolors
        for c in range(k, len(blocks)):
            if blocks[c] == 'W':
                recolors += 1
            if blocks[c-k] == 'W':
                recolors -= 1
            minRecolors = min(minRecolors, recolors)
        return minRecolors
                    
                 
            


