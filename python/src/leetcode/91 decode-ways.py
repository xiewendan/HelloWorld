# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/09 17:40:33

# desc: desc

# 一条包含字母 A-Z 的消息通过以下方式进行了编码：

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。

# 示例 1:

# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2:

# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 动态规划
# dp[i]
#       i = 0 if s[i] = [1,9] else 0
#       i = [1,n)   
#           if s[i] == 0:
#             if s[i-1] == 0:       0
#             elif s[i-1] = {1,2}   dp[i-2]
#             else:                 0
#           else:
#             if s[i-1,i] <= 9:     dp[i-1]
#             elif s[i-1,i] <= 26:  dp[i-1] + dp[i-2]
#             else:                 dp[i-1]

# 复杂度
## 时间复杂度：o(n)
## 空间复杂度：o(1)

# 代码
class Solution:
    def numDecodings(self, s: str) -> int:
        nLen = len(s)
        if nLen < 1:
            return 0
        if s[0] == '0':
            return 0
        if nLen == 1:
            return 1
        
        # 起码两个字符，开头不为0
        dp = [0] * nLen
        dp[0] = 1
        for i in range(1,nLen):
            if s[i] == '0':
                if s[i-1] in {'1', '2'}:
                    if i - 2 >= 0:
                        dp[i] = dp[i-2]
                    else:
                        dp[i] = 1
                else:
                    return 0
            else:
                lastTwoChar = int(s[i-1:i+1])
                if lastTwoChar <= 9:
                    dp[i] = dp[i-1]
                elif lastTwoChar <= 26:
                    if i - 2 >= 0:
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1]
        return dp[nLen-1]
    
# 边界
solution = Solution()
# len(s) == 0
assert(solution.numDecodings("") == 0)

# len(s) == 1
assert(solution.numDecodings("0") == 0)
assert(solution.numDecodings("1") == 1)
# len(s) == 2
assert(solution.numDecodings("00") == 0)
assert(solution.numDecodings("01") == 0)
assert(solution.numDecodings("09") == 0)
assert(solution.numDecodings("10") == 1)
assert(solution.numDecodings("20") == 1)
assert(solution.numDecodings("26") == 2)
assert(solution.numDecodings("27") == 1)
assert(solution.numDecodings("30") == 0)

# len(s) >= 3
assert(solution.numDecodings("000") == 0)
assert(solution.numDecodings("026") == 0)

assert(solution.numDecodings("100") == 0)
assert(solution.numDecodings("101") == 1)
assert(solution.numDecodings("110") == 1)
assert(solution.numDecodings("111") == 3)
assert(solution.numDecodings("127") == 2)

assert(solution.numDecodings("12") == 2)
assert(solution.numDecodings("226") == 3)