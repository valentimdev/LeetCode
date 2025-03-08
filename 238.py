class Solution(object):
    @classmethod
    def productExceptSelf(self, nums):
        output=[]
        mult_pre=1
        mult_su=1
        for i in range(len(nums)):
            try:
                if i<=0:
                    output.append(1)
                else:
                    mult_pre=nums[i-1]*mult_pre
                    output.append(mult_pre)
            except:
                output.append(mult_pre)
        print(output)
        for j in reversed(range(len(nums))):
            try:
                if j+1>=len(nums):
                    output_su.append(1)
                else:
                    mult_su=nums[j+1]*mult_su
                    output[j]*=mult_su
            except:
                continue
        return(output)

nums = [1,2,3,4]
print(Solution.productExceptSelf(nums))