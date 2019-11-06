# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/06 19:14:11

# desc: desc

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

# 网格中的障碍物和空位置分别用 1 和 0 来表示。

# 说明：m 和 n 的值均不超过 100。

# 示例 1:

# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 思路
# 动态规划：
# f[m][n] = 
#       障碍 0
#       不是障碍 f[m-1][n] + f[m][n-1]
# 复杂度（时间/空间）
# 时间
# 空间
# 代码
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    # def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        
        f = []
        for i in range(m):
            f.append([0] * n)
        
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                f[i][0] = 1
            else:
                break
        
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                f[0][i] = 1
            else:
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    f[i][j] = f[i-1][j] + f[i][j-1]
                else:
                    f[i][j] = 0
        
        return f[-1][-1]
    
# 边界
solution = Solution()
assert(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2)

