class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        currentNumber = 2
        number1 = 0
        number2 = 1
        
        while N>=currentNumber:
            ans = number1 + number2
            number1=number2
            number2=ans
            currentNumber+=1
        return ans
