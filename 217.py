class Solution(object):
    @classmethod
    def containsDuplicate(self, nums):
        hashset=set(nums)
        return (len(hashset)!=len(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution.containsDuplicate(nums))