# You are given a 0-indexed array nums of distinct integers. 
# You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

# More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

# Return any rearrangement of nums that meets the requirements.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums) - 1:
            l, r = i - 1, i + 1
            if nums[i] == (nums[l] + nums[r]) / 2:
                nums[i], nums[r] = nums[r], nums[i]
                i -= 1
            else:
                i += 1
            
        return nums

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        nums.sort()
        res = []
        
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1
            if l <= r:
                res.append(nums[r])
            r -= 1
        return res

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = [0] * len(nums)
        if len(nums) % 2 == 0:
            mid = len(nums) // 2 + 1
            median = nums[mid]
        else:
            mid = len(nums) // 2 
            median = nums[mid]
        
        j, n = 1, 0
        for i in range(len(nums)):
            if j < len(arr) and nums[i] < median:
                arr[j] = nums[i]
                j += 2
            else:
                arr[n] = nums[i]
                n += 2
        return arr