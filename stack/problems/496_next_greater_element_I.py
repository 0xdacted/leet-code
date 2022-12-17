# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            dq = deque(nums2)
            while dq[0] != n:
                dq.popleft()
            while dq and dq[0] <= n:
                dq.popleft()
            if dq:
                ans.append(dq[0])
            else:
                ans.append(-1)
        return ans

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        hm = {}
        
        for i, n in enumerate(nums1):
            hm[n] = i
            
        for i, n in enumerate(nums2):
            if n not in hm:
                continue
            else:
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > n:
                        ans[hm[n]] = nums2[j]
                        break
        return ans