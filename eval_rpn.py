from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                token1, token2 = stack.pop(), stack.pop()
                if token == "+": stack.append(token1 + token2)
                elif token == "-": stack.append(token1- token2)
                elif token == "*": stack.append(token1 * token2)
                else: stack.append(trunc(token1/ token2))
        return stack[0]

obj = Solution()   
n=int(input('Enter size of the token'))
tokens = list(map(str,input('Enter the tokens: ').strip().split()[:n]))
print(obj.evalRPN(tokens))