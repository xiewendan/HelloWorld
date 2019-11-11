# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/09 09:49:15

# desc: desc

# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

# 示例 1:

# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:

# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 动态规划
# dp[0] = 0
# dp[1] = 0
# dp[i] = s[i] 成对下标x的长度 + dp[x-1]
#       找不到s[i]成对下标   0
#       找到s[i]成对下标x   
#           x >=1           i-x+1 + dp[x-1]
#           x == 0          i - x + 1

# 复杂度（时间/空间）
# 时间  o(n*n)
# 空间  o(n)
# 代码
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        nLen = len(s)
        if nLen <= 1:
            return 0

        dp = [0] * (nLen)

        for i in range(1, nLen):
            if s[i] == '(':
                continue
            
            if s[i-1] == '(':
                if i >= 2:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            
            else:
                nPreIndex = i - dp[i-1] - 1

                if nPreIndex >= 0 and s[nPreIndex] == '(':
                    if nPreIndex == 0:
                        dp[i] = dp[i-1] + 2
                    else:
                        dp[i] = dp[i-1] + 2 + dp[nPreIndex - 1]
        
        nMax = 0
        for i in range(0, nLen):
            nMax = max(nMax, dp[i])

        return nMax

    
# 边界
solution = Solution()
# 空串
assert(solution.longestValidParentheses("") == 0)
# 单个字符
assert(solution.longestValidParentheses("(") == 0)
assert(solution.longestValidParentheses(")") == 0)
# 两个字符
assert(solution.longestValidParentheses("()") == 2)
assert(solution.longestValidParentheses(")(") == 0)
assert(solution.longestValidParentheses("))") == 0)
assert(solution.longestValidParentheses("((")== 0)

# 三个字符 共8种情况
assert(solution.longestValidParentheses(")))") == 0)
assert(solution.longestValidParentheses("())") == 2)
assert(solution.longestValidParentheses("(()") == 2)
assert(solution.longestValidParentheses("(((") == 0)

# 多个字符
## 两个没嵌套
assert(solution.longestValidParentheses("(()()(") == 4)
## 两个有嵌套
assert(solution.longestValidParentheses("(()())") == 6)
# 其它
assert(solution.longestValidParentheses(")()())") == 4)
