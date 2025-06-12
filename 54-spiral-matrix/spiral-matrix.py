class Solution:
    def spiralOrder(self, matrix):
        ans = []
        row = len(matrix)
        col = len(matrix[0])

        i = 0
        j = 0
        rsteps = row - 1
        csteps = col - 1
        count = 0

        while rsteps >= 1 and csteps >= 1:
            for k in range(csteps):
                ans.append(matrix[i][j])
                j += 1
                count += 1

            for k in range(rsteps):
                ans.append(matrix[i][j])
                i += 1
                count += 1

            for k in range(csteps, 0, -1):
                ans.append(matrix[i][j])
                j -= 1
                count += 1

            for k in range(rsteps, 0, -1):
                ans.append(matrix[i][j])
                i -= 1
                count += 1

            rsteps -= 2
            csteps -= 2
            i += 1
            j += 1

        if rsteps == 0:
            for k in range(csteps + 1):
                ans.append(matrix[i][j])
                j += 1
        elif csteps == 0:
            for k in range(rsteps + 1):
                ans.append(matrix[i][j])
                i += 1

        return ans

