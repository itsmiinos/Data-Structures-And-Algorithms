class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        basket = collections.defaultdict(int)
        max_length = 0

        while j < len(fruits) :
            if fruits[j] not in basket and len(basket) == 2:
                while i < len(fruits) and len(basket) == 2 :
                    basket[fruits[i]] -=1
                    if basket[fruits[i]] == 0 :
                        del basket[fruits[i]]
                    i+=1
                
            basket[fruits[j]]+=1

            max_length = max(max_length , j - i + 1)

            j+=1
        
        return max_length