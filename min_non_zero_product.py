class Solution:
	def minNonZeroProduct(self, p: int) -> int:
		highestDigit=2**p-1
		secondHighDigit=highestDigit-1
		numberOfPairs=highestDigit//2

		return (pow(secondHighDigit,numberOfPairs,1000000007)*highestDigit)%(1000000007)
