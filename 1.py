class Solution:
    @classmethod
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            index = nums.index(i)
            tamanho_lista = len(nums)
            while index < tamanho_lista - 1:
                soma = nums[index] + nums[index+1]
                index_1 = index
                index_2 = index +1
                index += 1
                if soma == target:
                    return [index_1,index_2]

nums=[3,2,3]
Solution.twoSum(nums,6)
