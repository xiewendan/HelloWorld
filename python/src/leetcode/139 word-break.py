# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/26 21:17:40

# desc: desc

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：

# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：

# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：

# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：

# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-break
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

# 代码
class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def wordBreak(self, s, wordDict):
        nLen = len(s)
        if nLen == 0:
            return True
        
        countSet = set()
        for word in wordDict:
            countSet.add(len(word))
        
        dp = [False] * (nLen+1)
        dp[0] = True

        for i in range(1, nLen+1):
            for count in countSet:
                if i - count >= 0 and s[i-count:i] in wordDict and dp[i-count]:
                    dp[i] = True
                    break
        
        return dp[nLen]
    
# 边界
solution = Solution()
# 零个单词
assert(solution.wordBreak("", []) == True)
assert(solution.wordBreak("leet", []) == False)
assert(solution.wordBreak("", ["leet"]) == True)

# 一个单词
assert(solution.wordBreak("leet", ["leet"]) == True)
assert(solution.wordBreak("lee", ["leet"]) == False)
assert(solution.wordBreak("leetleet", ["leet"]) == True)
assert(solution.wordBreak("leetlee", ["leet"]) == False)

# # 两个单词
assert(solution.wordBreak("leetcode", ["leet", "code"]) == True)
assert(solution.wordBreak("applepenapple", ["apple", "pen"]) == True)
assert(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)