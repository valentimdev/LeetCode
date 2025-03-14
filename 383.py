class Solution(object):
    @classmethod
    def canConstruct(self, ransomNote, magazine):
        i = set(ransomNote)
        j = set(magazine)
        print(i,j)
        return i in j
ransomNote = "aa"
magazine = "aab"
print(Solution.canConstruct(ransomNote,magazine))