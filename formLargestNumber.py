from array import array
import math
def largetNumber(numbers):
        temp=0
        output=""
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-i-1):
             num1=str(numbers[j])+str(numbers[j+1])
             num2=str(numbers[j+1])+str(numbers[j])
             num1Int = int(num1)
             num2Int = int(num2)
             if num1Int>num2Int:
              temp=numbers[j]
              numbers[j]=numbers[j+1]
              numbers[j+1]=temp
        for i in range(len(numbers)-1, -1, -1):
         output+=str(numbers[i])
        return output


n = int(input("Enter  size of list: "))
elements = list(map(list,input("\nEnter the elements : ").strip().split()))[:n]
output = largetNumber(elements)
print(output)
