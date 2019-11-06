# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/09/27 23:06:41

# desc: 是否匹配

# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:

# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3:

# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:

# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:

# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路：动态规划
# s[i,j] = 
#   0) s[:,0] = False, s[0,0] = True, s[0,:] 看情况 s[0,奇数] = False, p[2] = * 则s[0,2] = True, p[2n] = p[2n-2]
#   1) p[j] == .        s[i-1, j-1]
#   2) p[j] == *        
#       p[j-1] == s[i]   s[i-1, j] or s[i, j-1] or (s[i, j-2] if j > 2)
#       p[j-1] == .      s[i-1, j] or s[i, j-1] or (s[i, j-2] if j > 2)
#       p[j-1] == *      False
#       p[j-1] != s[i]   s[i, j-2]
#   3) p[j] == s[i]     s[i-1, j-1]
#   4) p[j] != s[i]     False
# 减枝：将p优化，如果存在相同的可以优化掉
# 复杂度（时间/空间）
# 时间 o(m*n)
# 空间 o(m*n)
# 代码
class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    def isMatch(self, s, p):
        nLenS = len(s)
        nLenP = len(p)

        subset = []
        for i in range(1+nLenS):
            subset.append([False]*(1+nLenP))
        for i in range(1+nLenS):
            subset[i][0] = False
        subset[0][0] = True

        for i in range(1,nLenP+1,2):
            subset[0][i] = False
            
        for i in range(2,nLenP+1,2):
            if p[i-1] == '*':
                subset[0][i] = subset[0][i-2]
            else:
                subset[0][i] = False

        for i in range(1, nLenS+1):
            curCharS = s[i-1]
            for j in range(1, nLenP+1):
                curCharP = p[j-1]

                if curCharP == '.' or curCharP == curCharS:
                    subset[i][j] = subset[i-1][j-1]
                elif curCharP == '*':
                    if j <= 1:
                        # assert(False)
                        return False        #
                    else:
                        if p[j-2] == '.' or p[j-2] == s[i-1]:
                            subset[i][j] = subset[i-1][j] or subset[i][j-1] or subset[i][j-2]
                        elif p[j-2] == '*':
                            # assert(False)
                            return False
                        else:
                            subset[i][j] = subset[i][j-2]

                else:
                    subset[i][j] = False
        
        return subset[nLenS][nLenP]

    
# 边界
solutionObj = Solution()

# 为空
assert(solutionObj.isMatch("", "") == True)# 0

assert(solutionObj.isMatch("", "aa") == False)# 0
assert(solutionObj.isMatch("aa", "") == False)# 0

# 只有字母
assert(solutionObj.isMatch("abc", "abc") == True)# 0

assert(solutionObj.isMatch("ab", "aa") == False)# 0
assert(solutionObj.isMatch("ab", "a") == False)# 0
assert(solutionObj.isMatch("a", "ab") == False)# 0

# 只有.
assert(solutionObj.isMatch("a", ".") == True)# 0
assert(solutionObj.isMatch("abc", "...") == True)# 0

assert(solutionObj.isMatch("ab", ".") == False)# 0
assert(solutionObj.isMatch("a", "..") == False)# 0

# 只有*
assert(solutionObj.isMatch("a", "*") == False)# 0
assert(solutionObj.isMatch("a", "**") == False)# 0
assert(solutionObj.isMatch("aa", "*") == False)# 0

# 字母+.
assert(solutionObj.isMatch("ab", ".b") == True)# 0
assert(solutionObj.isMatch("ab", "a.") == True)# 0

assert(solutionObj.isMatch("abc", ".ab") == False)# 0
assert(solutionObj.isMatch("abc", ".b") == False)# 0
assert(solutionObj.isMatch("ab", "ba.") == False)# 0

# 字母+*
assert(solutionObj.isMatch("aa", "a*") == True)# 0
assert(solutionObj.isMatch("aaaa", "a*") == True)# 0
assert(solutionObj.isMatch("aaaa", "a*a") == True)# 0

assert(solutionObj.isMatch("aa", "b*") == False)# 0
assert(solutionObj.isMatch("aaa", "b*") == False)# 0
assert(solutionObj.isMatch("aa", "b*a") == False)# 0
assert(solutionObj.isMatch("aa", "a**") == False)# 0

# .+*
assert(solutionObj.isMatch("abc", ".*") == True)# 0

# 字母+.+*
assert(solutionObj.isMatch("ab", ".*") == True)# 0
assert(solutionObj.isMatch("aab", ".*a*b") == True)# 0
assert(solutionObj.isMatch("aab", ".*a*b*") == True)# 0

# 未匹配
assert(solutionObj.isMatch("ab", "ab") == True)# 0
assert(solutionObj.isMatch("ab", "a") == False)# 0

# 已知
assert(solutionObj.isMatch("aa", "a") == False )# 0
assert(solutionObj.isMatch("mississippi", "mis*is*p*.") == False )# 0


assert(solutionObj.isMatch("aab", "c*a*b") == True)# 0
assert(solutionObj.isMatch("a", ".*..a*") == False)# 0
assert(solutionObj.isMatch("", ".*") == True)# 0