class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for si in s:
            if si == '(' or si == '{' or si == '[':
                stack.append(si)
            else:
                if len(stack) == 0:
                    return False
                result = stack[-1] + si
                del stack[-1]
                if result != '()' and result != '{}' and result != '[]':
                    return False
        if len(stack) > 0:
            return False
        return True
