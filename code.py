class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n, ans = len(nums), float("inf")

        for i in range(n):
            beg, end = i + 1, n - 1

            while beg < end:
                sm = nums[beg] + nums[end] + nums[i]
                ans = min(ans, sm, key = lambda x: abs(x - target))
        
                if sm <= target:
                    beg += 1
                elif sm > target:
                    end -= 1

        return ans

'''
we perform 2 pointers and look for sums which are around target
, that is if sum becomes bigger than target we move end pointer and in opposite case we move beg pointer.

Complexity
Time complexity is O(n^2), space is O(n) or O(log n) depening on sort function
'''



