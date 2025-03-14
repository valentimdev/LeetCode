class Solution(object):
    @classmethod
    def summaryRanges(self, nums):
        output = []
        i = 0
        while i < len(nums):
            number = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if number != nums[i]:
                output.append(f"{number} -> {nums[i]}")
            else:
                output.append(f"{nums[i]}")
            i += 1
        return output


nums = [0, 1, 2, 4, 5, 7]
print(Solution.summaryRanges(nums))
