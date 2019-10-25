# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/17 19:50:07

# desc: 

# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

# 请你实现这个将字符串进行指定行数变换的函数：

# string convert(string s, int numRows);
# 示例 1:

# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:

# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:

# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        nLen = len(s)
        if numRows >= nLen:
            return s
        
        if numRows <= 1:
            return s

        listlist = []
        for i in range(numRows):
            listlist.append([])
        
        nDir = 1
        nIndex = -1
        nMin = 0
        nMax = numRows - 1
        for nChar in s:
            nIndex += nDir

            listlist[nIndex].append(nChar)

            if nIndex == nMin:
                if nDir == -1:
                    nDir = 1
            elif nIndex == nMax:
                if nDir == 1:
                    nDir = -1
        
        newList = []
        for i in range(numRows):
            newList += listlist[i]
        
        return "".join(newList)

solution = Solution()
# 行数 > 字符串长度
assert(solution.convert("LEETCODEISHIRING", 100) == "LEETCODEISHIRING")

# 行数 == 字符串长度
assert(solution.convert("LEET", 4) == "LEET")

# 行数 < 字符串长度
## 行数 <= 1, 返回原字符串
assert(solution.convert("LEET", 0) == "LEET")
assert(solution.convert("LEET", 1) == "LEET")

## 行数 = 2
### 字符串长度 = 3
assert(solution.convert("abc", 2) == "acb")
### 字符串长度 = 4
assert(solution.convert("abcd", 2) == "acbd")
### 字符串长度 = 5
assert(solution.convert("abcde", 2) == "acebd")

## 行数 = 3
### 字符串长度 = 4
assert(solution.convert("abcd", 3) == "abdc")
### 字符串长度 = 5
assert(solution.convert("abcde", 3) == "aebdc")
### 字符串长度 = 6
assert(solution.convert("abcdef", 3) == "aebdfc")
### 字符串长度 = 7
assert(solution.convert("abcdefg", 3) == "aebdfcg")

# 其它
assert(solution.convert("LEETCODEISHIRING", 3) == "LCIRETOESIIGEDHN")
assert(solution.convert("LEETCODEISHIRING", 4) == "LDREOEIIECIHNTSG")