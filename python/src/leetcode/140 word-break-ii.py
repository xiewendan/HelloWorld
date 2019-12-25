# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/26 21:57:57

# desc: desc

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

# 说明：

# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：

# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：

# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 示例 3：

# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-break-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

# 代码
class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    def wordBreak(self, s, wordDict):
        nLen = len(s)
        if nLen == 0:
            return []
        
        countSet = set()
        for word in wordDict:
            countSet.add(len(word))
        
        dp = [False] * (nLen+1)
        dp[0] = True

        for i in range(1, nLen+1):
            for count in countSet:
                nLeftCount = i - count
                if nLeftCount >= 0 and dp[nLeftCount] and s[nLeftCount:i] in wordDict:
                    dp[i] = True
                    break

        if dp[nLen] is False:
            return []
        
        memoization = {}
        memoization[0] = []
        return self.wordBreakList(s, wordDict, dp, nLen, memoization, countSet)
    
    def wordBreakList(self, s, wordDict, dp, nLen, memoization, countSet):
        assert(dp[nLen])

        if nLen in memoization:
            return memoization[nLen]
        
        listRet = []
        for count in countSet:
            nLeftCount = nLen - count
            szEnd = s[nLeftCount:nLen]
            if nLeftCount >= 0 and dp[nLeftCount] and szEnd in wordDict:
                if nLeftCount == 0:
                    listRet.append(szEnd)
                else:
                    szEnd = ' ' + szEnd
                    listSubWord = self.wordBreakList(s, wordDict, dp, nLeftCount, memoization, countSet)

                    for subWord in listSubWord:
                        listRet.append(subWord + szEnd)
    
        memoization[nLen] = listRet

        return listRet
    
# 边界
solution = Solution()
# 零个单词
assert(solution.wordBreak("", []) ==[])
assert(solution.wordBreak("leet", []) == [])
assert(solution.wordBreak("", ["leet"]) == [])

# 一个单词
assert(solution.wordBreak("leet", ["leet"]) == ['leet'])
assert(solution.wordBreak("lee", ["leet"]) == [])
assert(solution.wordBreak("leetleet", ["leet"]) == ['leet leet'])
assert(solution.wordBreak("leetlee", ["leet"]) == [])

# 两个单词
assert(solution.wordBreak("leetcode", ["leet", "code"]) == ["leet code"])
assert(solution.wordBreak("applepenapple", ["apple", "pen"]) == ["apple pen apple"])
assert(solution.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]) == ["cats and dog","cat sand dog"])
assert(sorted(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(["pine applepen apple","pine apple pen apple","pineapple pen apple"]))
assert(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == [])

