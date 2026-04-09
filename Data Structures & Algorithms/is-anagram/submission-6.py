class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        sdit,tdit= {},{}
        for i in range(len(s)):
            sdit[s[i]] = 1 + sdit.get(s[i], 0)
            tdit[t[i]] = 1 + tdit.get(t[i], 0)

        return sdit == tdit
