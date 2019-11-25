# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/15 08:55:29

# desc: desc

# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

# 示例:

# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-rectangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
class Solution:
    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    def maximalRectangle(self, matrix):
        nRow = len(matrix)

        if nRow == 0:
            return 0
        
        nCol = len(matrix[0])
        if nCol == 0:
            return 0

        dp_heigh = [0] * nCol
        dp_left_w = [0] * nCol
        dp_right_w = [0] * nCol
        left_w = [0] * nCol
        right_w = [0] * nCol
        max_area = 0

        for i in range(nRow):
            # update left_w
            left_w[0] = int(matrix[i][0])
            for j in range(1, nCol):
                if matrix[i][j] == '0':
                    left_w[j] = 0
                else:
                    left_w[j] = left_w[j-1] + 1

            # update right_w
            right_w[nCol-1] = int(matrix[i][nCol-1])
            for j in range(nCol-2, -1, -1):
                if matrix[i][j] == '0':
                    right_w[j] = 0
                else:
                    right_w[j] = right_w[j+1] + 1

            for j in range(nCol):
                # 求高和面积
                if matrix[i][j] == '0':
                    dp_heigh[j] = 0
                    dp_left_w[j] = left_w[j]
                    dp_right_w[j] = right_w[j]
                else:
                    dp_heigh[j] = dp_heigh[j] + 1
                    if dp_left_w[j] == 0:
                        dp_left_w[j] = left_w[j]
                    else:
                        dp_left_w[j] = min(left_w[j], dp_left_w[j])

                    if dp_right_w[j] == 0:
                        dp_right_w[j] = right_w[j]
                    else:
                        dp_right_w[j] = min(right_w[j], dp_right_w[j])
                
                max_area = max(max_area, dp_heigh[j] * (dp_left_w[j] + dp_right_w[j]-1))
        
        return max_area
        
    
# 边界
solution = Solution()

# 0 x 0 矩阵
assert(solution.maximalRectangle([[]])==0)
    
# 1 x 1 矩阵
assert(solution.maximalRectangle([["0"]])==0)
assert(solution.maximalRectangle([["1"]])==1)

# 1 x 2 矩阵
assert(solution.maximalRectangle([["0", "0"]])==0)
assert(solution.maximalRectangle([["1", "0"]])==1)
assert(solution.maximalRectangle([["0", "1"]])==1)
assert(solution.maximalRectangle([["1", "1"]])==2)

# 2 x 1 矩阵
assert(solution.maximalRectangle([["0"],["0"]])==0)
assert(solution.maximalRectangle([["1"],["0"]])==1)
assert(solution.maximalRectangle([["0"],["1"]])==1)
assert(solution.maximalRectangle([["1"],["1"]])==2)

# 2 x 2 矩阵
assert(solution.maximalRectangle([["0", "0"],["0", "0"]])==0)
assert(solution.maximalRectangle([["0", "0"],["0", "1"]])==1)
assert(solution.maximalRectangle([["0", "1"],["0", "1"]])==2)
assert(solution.maximalRectangle([["1", "1"],["0", "1"]])==2)
assert(solution.maximalRectangle([["1", "1"],["1", "1"]])==4)

# 其它
assert(solution.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 6)

