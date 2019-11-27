# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/15 08:57:13

# desc: desc

# 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

# 下图是字符串 s1 = "great" 的一种可能的表示形式。

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# 在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

# 例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# 我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

# 同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# 我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

# 给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

# 示例 1:

# 输入: s1 = "great", s2 = "rgeat"
# 输出: true
# 示例 2:

# 输入: s1 = "abcde", s2 = "caebd"
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/scramble-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 递归：超出时间限制
# dp：

# 复杂度（时间/空间）
# 时间
# 空间
# 代码

## 方案一，递归
# class Solution:
#     # def isScramble(self, s1: str, s2: str) -> bool:
    # def isScramble(self, s1, s2):
    #     dictMemoization = {}
    #     return self.isScrambleMemo(s1, s2, dictMemoization)

    # def isScrambleMemo(self, s1, s2, dictMemorization):
    #     nLen1 = len(s1)
    #     nLen2 = len(s2)

    #     if nLen1 != nLen2:
    #         return False
        
    #     if nLen1 == 0:
    #         return True
        
    #     if s1 == s2:
    #         return True

    #     szS1S2 = s1 + "#" + s2
    #     if szS1S2 in dictMemorization:
    #         return dictMemorization[szS1S2]

    #     if sorted(s1) != sorted(s2):
    #         dictMemorization[szS1S2] = False
    #         return False

    #     # listLetterCount = [0] * 26
    #     # for i in range(nLen1):
    #     #     listLetterCount[ord(s1[i]) -ord('a')] += 1
    #     #     listLetterCount[ord(s2[i]) - ord('a')] -= 1

    #     # for count in listLetterCount:
    #     #     if count != 0:
    #     #         dictMemorization[szS1S2] = False
    #     #         return False


    #     for i in range(1, nLen1):
    #         bScrambleLeft = self.isScrambleMemo(s1[:i], s2[nLen1-1-i+1:], dictMemorization)
    #         bScrambleRight = self.isScrambleMemo(s1[i:], s2[:nLen1-i], dictMemorization)

    #         if bScrambleLeft and bScrambleRight:
    #             dictMemorization[szS1S2] = True
    #             return True
            
    #         bScrambleLeft = self.isScrambleMemo(s1[:i], s2[:i], dictMemorization)
    #         bScrambleRight = self.isScrambleMemo(s1[i:], s2[i:], dictMemorization)
    #         if bScrambleLeft and bScrambleRight:
    #             dictMemorization[szS1S2] = True
    #             return True

    #     dictMemorization[szS1S2] = False
    #     return False

## 方案二，动态规划
class Solution:
    # def isScramble(self, s1: str, s2: str) -> bool:
    def isScramble(self, s1: str, s2: str) -> bool:
        nLen1 = len(s1)
        nLen2 = len(s2)

        if nLen1 != nLen2:
            return False
        
        if nLen1 == 0:
            return True
        
        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False
        
        dp = []
        for k in range(nLen1+1):
            dp.append([])
            for i in range(nLen1):
                dp[k].append([False] * nLen1)
        
        for i in range(nLen1):
            for j in range(nLen1):
                dp[1][i][j] = s1[i] == s2[j]
        
        for k in range(2, nLen1+1):
            for i in range(nLen1 - k+1):
                for j in range(nLen1 - k+1):
                    for m in range(1,k):
                        dp[k][i][j] = (dp[m][i][j] and dp[k-m][i+m][j+m]) or (dp[m][i][j+k-m] and dp[k-m][i+m][j])

                        if dp[k][i][j]:
                            break
        
        return dp[nLen1][0][0]





        
        # a = []
        # for k in range(1,len):
        #     pass
        
    
# 边界
solution = Solution()

# 空
# assert(solution.isScramble("", "") == True)
# assert(solution.isScramble("", "a") == False)

# # 一个字符
# assert(solution.isScramble("a", "a") == True)
# assert(solution.isScramble("b", "a") == False)

# # 两个字符
# assert(solution.isScramble("ab", "ba") == True)
# assert(solution.isScramble("bc", "ba") == False)


print(solution.isScramble("great", "rgeat"))
# assert(solution.isScramble("great", "rgeat") == True)
# assert(solution.isScramble("abcde", "caebd") == False)