class Solution:
  def partition(self, elements, low, high):
    pivotElement = elements[high]
    pointer = low-1
 
    for i in range(low, high):
      if elements[i]<pivotElement:
        pointer+=1
        elements[pointer], elements[i] = elements[i], elements[pointer]
    elements[pointer+1], elements[high] = elements[high], elements[pointer+1]  
    return pointer+1
  def kthLargestNumber(self, elements, low, high):
    if low< high:
      pi = self.partition(elements, low, high)
      self.kthLargestNumber(elements, low, pi-1)
      self.kthLargestNumber(elements, pi+1, high)
      

n = int(input("Enter number of elements : "))   
elements = list(map(int,input("\nEnter the elements : ").strip().split()))[:n]
kthLargestNumber(elements, 0, n-1)
k = int(input("Enter  index: "))
print(elements[k])