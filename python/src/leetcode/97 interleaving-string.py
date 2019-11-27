# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/15 08:58:15

# desc: desc

# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

# 示例 1:

# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 示例 2:

# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/interleaving-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 动态规划

# 复杂度（时间/空间）
# 时间
# 空间
# 代码
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        nLen1 = len(s1)
        nLen2 = len(s2)
        nLen3 = len(s3)

        # 长度边界检查
        if nLen1 == 0:
            return s2 == s3
        
        if nLen2 == 0:
            return s1 == s3
        
        if nLen1 + nLen2 != nLen3:
            return False
        
        # 检查计数是否正常
        dictChar2Count = {}
        for char in s1:
            if char not in dictChar2Count:
                dictChar2Count[char] = 1
            else:
                dictChar2Count[char] += 1

        for char in s2:
            if char not in dictChar2Count:
                dictChar2Count[char] = 1
            else:
                dictChar2Count[char] += 1

        for char in s3:
            if char not in dictChar2Count:
                return False                # s3存在s1和s2中不存在的字符
            else:
                dictChar2Count[char] -= 1
        
        for char, count in dictChar2Count.items():
            if count != 0:
                return False
        
        dp = []
        for i in range(nLen1+1):
            dp.append([False] * (nLen2 + 1))
        
        dp[0][0] = True

        for i in range(1, nLen1 + 1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
            else:
                break
        
        for j in range(1, nLen2 + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
            else:
                break
        
        for i in range(1, nLen1 + 1):
            for j in range(1, nLen2 + 1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
            
        return dp[nLen1][nLen2]
    
# 边界
solution = Solution()

# 0, 0
assert(solution.isInterleave("", "", "") == True)

# 0, 1
assert(solution.isInterleave("", "a", "a") == True)

# 1, 0
assert(solution.isInterleave("a", "", "a") == True)

# 1, 1
assert(solution.isInterleave("a", "b", "ab") == True)
assert(solution.isInterleave("a", "b", "ba") == True)
assert(solution.isInterleave("a", "b", "aa") == False)

# 2, 1
assert(solution.isInterleave("ab", "c", "abc") == True)
assert(solution.isInterleave("ab", "c", "acb") == True)
assert(solution.isInterleave("ab", "c", "cab") == True)
assert(solution.isInterleave("ab", "c", "cba") == False)

# n, n
assert(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True)
assert(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False)

