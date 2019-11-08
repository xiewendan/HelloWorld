# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/08 19:27:18

# desc: desc

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例:

# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# i = 0, dp[0][j] = grid[0][j] + dp[0][j-1]
# j = 0, dp[i][0] = grid[i][0] + dp[i-1][0]
# i > 0 and j > 0, dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
# 复杂度（时间/空间）
# 时间 o(m*n)
# 空间 n(m*n)
# 代码
class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid) -> int:
        m = len (grid)
        if m == 0:
            return 0

        n = len(grid[0])
        if n == 0:
            return 0
        
        dp = []
        for i in range(m):
            dp.append([0] * n)
        
        dp[0][0] = grid[0][0]

        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]
    
# 边界
solution = Solution()
# m = 0 or n = 0
assert(solution.minPathSum([])==0)
assert(solution.minPathSum([[]])==0)

# m = 1, n = 1
assert(solution.minPathSum([[10]])==10)

# m = 1, n = 2
assert(solution.minPathSum([[10,1]])==11)

# m = 2, n = 1
assert(solution.minPathSum([[10],[1]])==11)

# m = 2, n = 2
assert(solution.minPathSum([[1, 2],[1, 5]])==7)
assert(solution.minPathSum([[1, 0],[1, 5]])==6)

# m = 3, n = 3
assert(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7)