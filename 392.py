class Solution:
    @classmethod
    def isSubsequence(self, s: str, t: str) -> bool:
        try:
            first = s[0]
        except:
            return True
        return_word=""
        counter=0
        tamanho=len(s)
        for word in t:
            if word == s[counter]:
                return_word+=word
                if return_word == s:return True
                counter+=1
        return return_word == s
s = "b"
t = "abc"
print(Solution.isSubsequence(s,t))