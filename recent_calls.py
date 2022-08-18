from collections import deque
class RecentCalls:
    def __init__(self):
        self.a = deque()
    def ping(self, t: int)->int:
        if len(self.a)==0:
            self.a.append(t)
            return 1
        while t-self.a[0]>3000:
            self.a.popleft()
            if len(self.a)==0:
                self.a.append(t)
                break
        else:
            self.a.append(t)
        return len(self.a)
output = []
obj = RecentCalls()

size=int(input('Enter size: '))
elements = list(map(int,input('Enter elements: ').strip().split()[:size]))

for i, item in enumerate(elements):
 output.append(obj.ping(item))
print(output)