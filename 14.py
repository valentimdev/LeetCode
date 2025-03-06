class Solution:
    @classmethod
    def longestCommonPrefix(self, strs):
        output=""
        count= 0
        first=strs[0]
        output_counter = 0
        for letter in first:
            try:
                for word in strs:
                    if word[count] != letter:
                        return output
                    if word[count] == letter:
                        output_counter+=1
                    if output_counter == len(strs):
                        output+=letter
                output_counter=0
                count+=1
            except:
                return output
        return output
        


strs = ["cir","car"]
print((Solution.longestCommonPrefix(strs)))
