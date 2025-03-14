class Solution:
    @classmethod
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dicionario={}
        retorno=0
        for index,num in enumerate(nums):
            if num in dicionario:
                retorno = index-dicionario[num]
                if abs(retorno) <= k:
                    return True
            dicionario[num]=index
        return abs(retorno)==k
nums = [99,99]
k = 2
print(Solution.containsNearbyDuplicate(nums,k))