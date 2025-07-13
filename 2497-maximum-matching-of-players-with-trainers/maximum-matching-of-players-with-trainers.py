class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        j = 0 
        count = 0
        for player in players : 

            while j < len(trainers) and trainers[j] < player : 
                j+=1
            
            if j < len(trainers) and player <= trainers[j] : 
                count+=1
                j+=1
        
        return count