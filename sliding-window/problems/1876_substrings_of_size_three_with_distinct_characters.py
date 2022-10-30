# 1876. Substrings of size three with distinct characters
# A string is good if there are no repeated characters
# Given a string 's', return the number of good substrings of length three in s
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted
# A substring is a contiguous sequence of characters in a string
def countGoodSubstrings(self, s: str) -> int:
        hm = {}
        count = 0
        windowStart = 0
        for windowEnd, c in enumerate(s):
            while c in hm.values():
                hm.pop(windowStart)
                windowStart += 1
            if len(hm) + 1 == 3:
                count += 1
                hm.pop(windowStart)
                windowStart += 1
            hm[windowEnd] = c
        return count