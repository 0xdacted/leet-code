# There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

# A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100

# Otherwise, x will send a friend request to y.

# Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

# Return the total number of friend requests made.

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        counter = collections.Counter(ages)
        res = 0
        for ageA, countA in counter.items():
            for ageB, countB in counter.items():
                if ageB <= (0.5 * ageA) + 7:
                    continue
                if ageB > ageA:
                    continue
                res += countA * countB
                if ageA == ageB:
                    res -= countA
        return res