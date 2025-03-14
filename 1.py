class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        view = {}
        for index, valor in enumerate(nums):
            complemento = target - valor
            if complemento in view:
                return [view[complemento], index]
            else:
                view[valor] = index