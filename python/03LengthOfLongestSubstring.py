# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/08/19 12:29:48

# desc: 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# bug1: 获得字符串长度 len(s)
# bug2: 删除dict中的keyvalue pair：用del方法

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # one character or ""
        nLength = len(s)
        if nLength <= 1:
            return nLength

        # two or more character
        nStart = 0
        nEnd = 1
        dictChar2Index = {}
        dictChar2Index[s[0]] = 0
        nMaxLength = 1

        strNew = s + s[nLength - 1]

        while nEnd < nLength:
            while strNew[nEnd] not in dictChar2Index:
                dictChar2Index[strNew[nEnd]] = nEnd
                nEnd +=1
            if nEnd - nStart > nMaxLength:
                nMaxLength = nEnd-nStart

            nNewStart = dictChar2Index[strNew[nEnd]] + 1
            while nStart < nNewStart:
                del dictChar2Index[strNew[nStart]] 
                nStart += 1
        
        return nMaxLength


solutionObj = Solution()
assert(solutionObj.lengthOfLongestSubstring("") == 0) # 0

assert(solutionObj.lengthOfLongestSubstring("a") == 1) # 1

assert(solutionObj.lengthOfLongestSubstring("aa") == 1) # 1
assert(solutionObj.lengthOfLongestSubstring("ab") == 2) # 2

assert(solutionObj.lengthOfLongestSubstring("aba")) # 2
assert(solutionObj.lengthOfLongestSubstring("abcabcbb")) # 3
assert(solutionObj.lengthOfLongestSubstring("bbbbb")) # 1
assert(solutionObj.lengthOfLongestSubstring("pwwkew")) # 3



