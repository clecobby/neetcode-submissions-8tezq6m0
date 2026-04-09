class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(","]":"[","}":"{"}
        stackk=[]
        for close in s:
            if close in Map:
                if stackk and stackk[-1]==Map[close]:
                    stackk.pop()
                else:
                    return False
            else:
                stackk.append(close)  
        return True if not stackk else False