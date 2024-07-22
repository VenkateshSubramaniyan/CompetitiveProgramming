class Paranthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        OpenClose = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in OpenClose.keys():
                stack.append(i)
            elif i in OpenClose.values():
                if (not len(stack) == 0 and i == OpenClose[stack[-1]]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


main = Paranthesis()
s = "{[]}"
result = main.isValid(s)
print(result)
