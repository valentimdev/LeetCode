class Solution:
    @classmethod
    def romanToInt(self, s: str) -> int:
        result = 0
        before = ""
        for i in s:
            if i == "I":
                result+=1
                before=i
            if i == "V" and before != "I":
                result+=5 
                before=i
            elif i == "V" and before == "I":
                result+=3
                before=i
            if i == "X" and before != "I":
                result+=10
                before=i   
            elif i == "X" and before == "I":
                result+=8
                before=i   
            if i == "L" and before != "X":
                result+=50  
                before = i
            elif i == "L" and before == "X":
                result+=30
                before = i
            if i == "C" and before != "X":
                result+=100
                before=i  
            elif i == "C" and before == "X":
                result+=80
                before=i  
            if i == "D" and before != "C":
                result+=500
                before = i
            if i == "D" and before == "C":
                result+=300
                before = i
            if i == "M" and before != "C":
                result+=1000
                before = i
            elif i == "M" and before == "C":
                result+=800
                before = i
        return result
print(Solution.romanToInt("MCDLXXVI"))