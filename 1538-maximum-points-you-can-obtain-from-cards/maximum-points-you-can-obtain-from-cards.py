class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = 0
        for i in range(k) :
            max_sum += cardPoints[i]
        
        total_sum = max_sum
        i = 0
        j = k-1
        a = len(cardPoints)-1

        while a > len(cardPoints) - k - 1 :
            total_sum += cardPoints[a]

            total_sum -= cardPoints[j]
            j-=1

            max_sum = max(total_sum , max_sum)

            a-=1
        
        return max_sum