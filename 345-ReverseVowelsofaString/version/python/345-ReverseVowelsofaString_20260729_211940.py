# Last updated: 7/29/2026, 9:19:40 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
4        my_vowels = []
5        for i in range(len(s)-1 , -1 , -1) :
6            if s[i] in vowels :
7                my_vowels.append(s[i])
8        print(my_vowels)
9        j = 0
10        for i in range(len(s)) :
11            if s[i] in vowels :
12                s = s[:i] + my_vowels[j] + s[i+1 :]
13                j+=1
14        
15        return s