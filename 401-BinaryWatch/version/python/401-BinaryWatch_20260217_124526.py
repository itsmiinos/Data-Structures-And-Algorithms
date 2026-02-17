# Last updated: 2/17/2026, 12:45:26 PM
1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        ans = []
4        for hour in range(0 , 12) :
5            for minutes in range(0 , 60) :
6                if self.countBits(hour , minutes) == turnedOn :
7                    if minutes <= 9 :
8                        ans.append(str(hour) + ":0" + str(minutes))
9                    else :
10                        ans.append(str(hour) + ":" + str(minutes))
11        
12        return ans
13    
14    def countBits(self , hour : int , minutes : int) -> int :
15        count = 0
16
17        for i in range(0 , 32) :
18            if (hour >> i) & 1 == 1 :
19                count+=1
20            
21        for i in range(0 , 32) :
22            if (minutes >> i) & 1 == 1 :
23                count+=1
24        
25        return count