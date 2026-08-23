class Solution:
    def sumGame(self, num: str) -> bool:
        left_marks = 0
        right_marks = 0
        left_known_sum = 0
        right_known_sum = 0

        for i in range(len(num)) :
            if i < len(num) / 2 :
                if num[i] == '?' :
                    left_marks +=1
                else :
                    left_known_sum += int(num[i])
            else :
                if num[i] == '?' :
                    right_marks +=1
                else :
                    right_known_sum += int(num[i])

        if (left_marks + right_marks) % 2 != 0 :
            return True
        
        left_total = (2 * left_known_sum) + (9 * left_marks)
        right_total = (2 * right_known_sum) + (9 * right_marks)

        if left_total == right_total :
            return False
        
        return True