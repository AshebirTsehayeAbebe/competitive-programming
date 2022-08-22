class Solution:
    def checkIfPaired(self, left, right):
        return left=='{' and right=='}' or left=='(' and right==')' or left=='[' and right==']'
    def isValid(self, s: str) -> bool:
        stack=[]
        for item in s:
            if item=='(' or item=='{' or item=='[':
                stack.append(item)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not self.checkIfPaired(top, item):                    
                    return False
        
        if not stack:
            return True
        else:
            return False
obj= Solution()
s=int(input('Enter the string: '))
print(obj.isValid(s))


