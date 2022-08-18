from typing import List
class Solution:
    def fizzBuzz(self, n: List[str]) -> str:
            answer = []
            for i in range(1, n + 1):
                if i % 3 == 0 and i % 5 == 0:
                    answer.append("FizzBuzz")
                elif i % 3 == 0:
                    answer.append("Fizz")
                elif (i % 5 == 0):
                    answer.append("Buzz")
                else:
                    answer.append(str(i))

            return answer;
n = int(input("Enter your value: "))
obj =Solution()
print(obj.fizzBuzz(n))
