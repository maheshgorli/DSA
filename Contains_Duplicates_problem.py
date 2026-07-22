class Solution:
    def containsDuplicate(self, nums):
        hset = set()
        for n in nums:
            if n in hset:
                return True
            hset.add(n)
        return False

sol = Solution()
nums = [1, 2, 3, 1]
print(sol.containsDuplicate(nums))