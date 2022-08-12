def heapify(arr, n, i):
  largest = i
  left = 2*i+1
  right = 2*i+2
  
  if left<n and arr[left]>arr[largest]:
    largest= left
  if right<n and arr[right]>arr[largest]:
    largest= right
  if largest!=i:
   arr[i], arr[largest]=arr[largest], arr[i]
   heapify(arr, n, largest)

def heapSort(arr):
  n= len(arr)
#Build max heap   
  for i in range(n//2,-1,-1):
    heapify(arr, n, i)
#Swap and remove root element    
  for i in range(n-1,0,-1):
    arr[i], arr[0]=arr[0],arr[i]
    heapify(arr, i, 0)
  
arr=[1,2,8,4,7,6,5]
heapSort(arr)
for i in range(0, len(arr)):
 print(arr[i])
    
