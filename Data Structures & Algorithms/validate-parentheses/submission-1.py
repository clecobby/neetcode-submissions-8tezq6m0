class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(","]":"[","}":"{"}
        stackk=[]
        for i in s:
            if i not in Map:
                stackk.append(i)
                continue
            if not stackk or stackk[-1]!=Map[i]:
                return False
            stackk.pop()
        return not stackk