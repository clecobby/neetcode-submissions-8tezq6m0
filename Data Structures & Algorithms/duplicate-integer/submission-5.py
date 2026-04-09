


class Solution():


    def hasDuplicate(self, liste : List[int])-> bool:

        seen = set()
        for i in liste:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False