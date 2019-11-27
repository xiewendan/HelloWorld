# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/15 08:59:04

# desc: desc
# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

# 示例 1:

# 输入: S = "rabbbit", T = "rabbit"
# 输出: 3
# 解释:

# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 示例 2:

# 输入: S = "babgbag", T = "bag"
# 输出: 5
# 解释:

# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)

# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/distinct-subsequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# dp[i][j] = # s中前i个字符和t前j个字符计算得到个个数
#           dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)
# dp[0][0] = 1
# dp[i][0] = 0 if i > 0 else 1
# dp[0][j] = 0 if j > 0 else 1

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        nLenS = len(s)
        nLenT = len(t)
        
        if nLenS < nLenT:
            return 0

        dp = []
        nLenSPlus1 = nLenS + 1
        for i in range(nLenSPlus1):
            dp.append([0] * (nLenT+1))
        
        for i in range(nLenSPlus1):
            dp[i][0] = 1

        for i in range(1, nLenSPlus1):
            rangeT = min(i, nLenT) + 1
            for j in range(1, rangeT):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[nLenS][nLenT]
    
# 边界
solution = Solution()

# 0 0
assert(solution.numDistinct("", "") == 1)

# 1 0
assert(solution.numDistinct("a", "") == 1)

# 0 1
assert(solution.numDistinct("", "a") == 0)

# 1 1
assert(solution.numDistinct("b", "a") == 0)
assert(solution.numDistinct("a", "a") == 1)

# 2 1
assert(solution.numDistinct("bc", "a") == 0)
assert(solution.numDistinct("ba", "a") == 1)
assert(solution.numDistinct("aa", "a") == 2)

# 1 2   不可能
assert(solution.numDistinct("a", "ab") == 0)

# 长度
assert(solution.numDistinct("rabbbit", "rabbit") == 3)
assert(solution.numDistinct("babgbag", "bag") == 5)