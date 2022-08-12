from array import array
import math
def kClosest(self, points, k):
        output=[]
        for i in range(1, len(points)):
            j=i-1
            key=points[i]
            keyDistance = math.sqrt(key[0]*key[0]+key[1]*key[1])
            currentItemDistance = math.sqrt(points[j][0]*points[j][0]+points[j][1]*points[j][1])
            while(j>=0 and keyDistance < currentItemDistance):
                points[j+1]=points[j]
                j-=1
                currentItemDistance = math.sqrt(points[j][0]*points[j][0]+points[j][1]*points[j][1])
            points[j+1]=key
        for i in range(k):
            output.append(points[i])
            
        return output


n = int(input("Enter the number of points : "))
points = list(map(list,input("\nEnter the points : ").strip().split()))[:n]
print(points)
kClosest(points, 1)
