# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/08 20:11:07

# desc: desc

# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 示例 1:

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:

# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:

# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:

# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:

# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/wildcard-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# dp[i][j] =                i,j表示第几个字符，和字符下标需要减一操作
#   p[j-1] == '?'     dp[i-1][j-1]
#   p[j-1] == s[i-1]    dp[i-1][j-1]
#   p[j-1] == '*'     
#                   0   dp[i][j-1]          or
#                   1   dp[i-1][j-1]        or
#                   n   dp[i-1][j]
#   p[j-1] != s[i-1]    False
#
#   i = 0            
#       p[j-1] == *   dp[0][j] = dp[0][j-1]
#       p[j-1] != *   dp[0][j] = False
#   j = 0
#                     dp[i][0] = False
#   i = 0, j = 0      dp[0][0] = True


# 复杂度（时间/空间）
# 时间 o(m*n)
# 空间 o(m*n)
# 代码
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = []
        for i in range(m+1):
            dp.append([False] * (n+1))
        
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

            elif p[j-1] != '*':
                break
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                # else:
                #     dp[i][j] = False

        return dp[m][n]
    
# 边界
solution = Solution()

# p类型


# 其它
assert(solution.isMatch("aa", "a") == False)
assert(solution.isMatch("aa", "*") == True)
assert(solution.isMatch("cb", "*a") == False)
assert(solution.isMatch("adceb", "*a*b") == True)
assert(solution.isMatch("acdcb", "a*c?b") == False)