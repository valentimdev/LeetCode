class Solution:
    @classmethod
    def findClosestNumber(self, nums: list[int]) -> int:
        menor = 100000000000000000000
        for num in nums:
            if num==0:
                return 0
            if abs(num)<abs(menor):
                menor=num
            if num == -menor:
                menor = abs(menor)
        return menor


def main():
    nums = [-4,-2,1,4,8]
    print(Solution.findClosestNumber(nums))

if __name__ == "__main__":
    main()