# Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays 
# such that the value of the maximum array element in that subarray is in the range [left, right].

# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        r = l = -1
        for i, n in enumerate(nums):
            if n <= right and n >= left:
                r = i
            if n > right:
                l = r = i
                continue
            res += r - l
        return res