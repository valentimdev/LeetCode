class Solution:
    @classmethod
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        loop=0
        word3=""
        if len(word1)>=len(word2):
            loop=len(word1)
        else:
            loop=len(word2)
        for i in range(loop):
            try:
                word3+=word1[i]+word2[i]
            except IndexError:
                if(len(word1)>=len(word2)):
                    word3+=word1[i]
                else:
                    word3+=word2[i]
        return word3
word1 = "abcd"
word2 = "pq"
print(Solution.mergeAlternately(word1,word2))