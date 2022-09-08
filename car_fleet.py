class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair, stack = [], []
        aa=[[1,5],[4,0],[3,1]]
        aa.sort(reverse=True)
        print(aa)
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        pair.sort(reverse=True)
        for i in range(len(pair)):
                         time = (target - pair[i][0]) / pair[i][1]
                         if stack:
                            if time > stack[-1]:
                                stack.append(time)
                         else:
                            stack.append(time)
        return len(stack)
