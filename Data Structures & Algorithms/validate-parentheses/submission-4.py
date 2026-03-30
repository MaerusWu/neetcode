class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False

        map = {')':'(', ']':'[', '}':'{'}
        stack = list()
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if  char == ')' or char == ']' or char == '}':
                if len(stack) == 0: return False
                if map[char] == stack[-1]:
                        stack.pop()
                else: return False

        if len(stack) == 0:
            return True
        return False