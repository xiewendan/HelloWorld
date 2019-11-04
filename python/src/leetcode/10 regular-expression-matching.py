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

# 思路
# 1、如果*不是贪心算法，则需要处理p：p中，*前面的字符和*后面的字符相同，则将*后面的那个字符删除，确保 aaa和a*a匹配。
# 2、两个指针，a指向s的第一个字符，b指向p的第一个字符。根据情况移动指针
#    2.1、b所指字符是*，则循环移动a指向字符，直到与b的last字符不等
#    2.2、a,b所指向字符不等，则直接停止
#    2.3、a,b所指向字符相等，则同时移动a，b
# 3、判断两个指针是否都指向末尾，是的话则匹配；否则不匹配
# 复杂度（时间/空间）
# 时间 o(n)
# 空间 o(1)
# 代码
class Solution:
    def isMatch(self, s, p):
        nLenS = len(s)
        nLenP = len(p)

        # if nLenS == 0:
        #     if nLenP == 0:
        #         return True
        #     else:
        #         return False
        # else:
        #     if nLenP == 0:
        #         return False
        
        if nLenP > 0 and p[0] == "*":
            return False
        
        nIndexS = 0
        nIndexP = 0

        lastCharP = ""
        while nIndexS < nLenS and nIndexP < nLenP:
            curCharS = s[nIndexS]
            curCharP = p[nIndexP]

            if curCharP == "*":
                if self.isCharEqual(curCharS, lastCharP):
                    nIndexS += 1
                else:
                    nIndexP += 1
                    lastCharP = curCharP

            else:
                if self.isCharEqual(curCharS, curCharP):
                    nIndexS += 1
                    nIndexP += 1
                    lastCharP = curCharP
                    continue
                else:
                    return False

        while nIndexP < nLenP:
            curCharP = p[nIndexP]

            if lastCharP == "*":
                if curCharP == "*":
                    break
                else:
                    lastCharP = curCharP
                    nIndexP += 1
            else:
                if curCharP == "*":
                    lastCharP = curCharP
                    nIndexP += 1
                else:
                    break

        return nIndexS == nLenS and nIndexP == nLenP

    def isCharEqual(self, a, b):
        return b == '.' or a == b
    
    def isCharSame(self, a, b):
        return a == b
    
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
# assert(solutionObj.isMatch("aaaa", "a*a") == True)# 0

assert(solutionObj.isMatch("aa", "b*") == False)# 0
assert(solutionObj.isMatch("aaa", "b*") == False)# 0
assert(solutionObj.isMatch("aa", "b*a") == False)# 0
assert(solutionObj.isMatch("aa", "a**") == False)# 0

# .+*
assert(solutionObj.isMatch("abc", ".*") == True)# 0

# 字母+.+*
assert(solutionObj.isMatch("ab", ".*") == True)# 0
# assert(solutionObj.isMatch("aab", ".*a*b") == True)# 0
# assert(solutionObj.isMatch("aab", ".*a*b*") == True)# 0

# 未匹配
assert(solutionObj.isMatch("ab", "ab") == True)# 0
assert(solutionObj.isMatch("ab", "a") == False)# 0

# 已知
assert(solutionObj.isMatch("aa", "a") == False )# 0
assert(solutionObj.isMatch("mississippi", "mis*is*p*.") == False )# 0