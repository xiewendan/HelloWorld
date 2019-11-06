# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/06 19:13:52

# desc: desc

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 问总共有多少条不同的路径？

# 例如，上图是一个7 x 3 的网格。有多少可能的路径？

# 说明：m 和 n 的值均不超过 100。

# 示例 1:

# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:

# 输入: m = 7, n = 3
# 输出: 28

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 思路
# 采用动态规划
# f(m,n) = f(m-1,n) + f(m, n-1)
# f(:,0) = 1
# f(0,:) = 1

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        if m == 1 or n == 1:
            return 1

        f = {}
        for i in range(m+1):
            f[i]= {}
            f[i][1] = 1
        for i in range(n+1):
            f[1][i] = 1
        
        for i in range(2, m+1):
            for j in range(2, n+1):
                f[i][j] = f[i-1][j] + f[i][j-1]
        
        return f[m][n]
    
# 边界
solution = Solution()

# ## 有一个为0
# assert(solution.uniquePaths(0,0)==0)
# assert(solution.uniquePaths(10,0)==0)
# assert(solution.uniquePaths(0,10)==0)

# ## 1x1
# assert(solution.uniquePaths(0,0)==0)

# ## 1x2
# assert(solution.uniquePaths(1,2)==1)

# ## 2x1
# assert(solution.uniquePaths(2,1)==1)

## 2x2
assert(solution.uniquePaths(2,2)==2)

## 3x2
assert(solution.uniquePaths(3,2)==3)

