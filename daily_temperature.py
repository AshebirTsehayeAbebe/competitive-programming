class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0]*len(temperatures)        
        stack = []
        for i in range(len(temperatures)):
            while stack:
                index = stack[len(stack)-1]
                if temperatures[i] <= temperatures[index]:
                    break
                stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
