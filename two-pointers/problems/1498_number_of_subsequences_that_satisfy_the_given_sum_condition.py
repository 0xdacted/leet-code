# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        count = left = 0
        right = len(nums) - 1
        while left < len(nums) and nums[left] * 2 <= target:
            while nums[left] + nums[right] > target:
                right -= 1
            count += pow(2, right - left)
            left += 1
            
        return count%(10**9 + 7)


  class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        mod = 10**9 + 7
        r = n-1
        
        
        for l in range(n):
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
            if l <= r:
                res += pow(2, r- l, mod)
                res %= mod
        return res