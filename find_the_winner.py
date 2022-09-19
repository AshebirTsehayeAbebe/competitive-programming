class Solution :
    def  findTheWinner(self, n,  k) :
        return self.findWinnerHelper(n, k - 1) + 1
    def  findWinnerHelper(self, n,  k) :
        if (n == 1) :
            return 0
        return ((k + 1) % n + self.findWinnerHelper(n - 1, k)) % n
