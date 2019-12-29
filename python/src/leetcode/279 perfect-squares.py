# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/12/28 21:15:27

# desc: desc

# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

# 示例 1:

# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
# 示例 2:

# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-squares
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 动态规划

# 代码


class Solution:
    def numSquares(self, n):
        dp = [0] * (n+1)

        listSquare = []
        nSqrt = int(n ** 0.5)
        for i in range(1, nSqrt+1):
            listSquare.append(i*i)
        
        for i in range(1, n + 1):
            nMin = i
            for nSquare in listSquare:
                if i >= nSquare:
                    nMin = min(nMin, dp[i - nSquare])
                else:
                    break

            dp[i] = nMin + 1
        
        return dp[-1]


# 边界
solution = Solution()
# 0
# assert(solution.numSquares(0) == 0)
# 1
assert(solution.numSquares(1) == 1)
# 2
assert(solution.numSquares(2) == 2)
# 3
assert(solution.numSquares(3) == 3)
assert(solution.numSquares(4) == 1)
assert(solution.numSquares(5) == 2)
assert(solution.numSquares(6) == 3)
assert(solution.numSquares(7) == 4)
assert(solution.numSquares(8) == 2)
assert(solution.numSquares(9) == 1)
assert(solution.numSquares(10) == 2)
assert(solution.numSquares(11) == 3)
assert(solution.numSquares(12) == 3)
assert(solution.numSquares(13) == 2)
