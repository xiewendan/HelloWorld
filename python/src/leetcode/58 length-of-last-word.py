# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/18 12:45:31

# desc: desc

# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

# 如果不存在最后一个单词，请返回 0 。

# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。

# 示例:

# 输入: "Hello World"
# 输出: 5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/length-of-last-word
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        nSpaceIndex = s.rfind(' ')
        if nSpaceIndex == -1:
            return len(s)
        return len(s[nSpaceIndex+1:])
    
solution = Solution()

assert(solution.lengthOfLastWord("Hello World") == 5)

# 没有空格
## 没有字符
assert(solution.lengthOfLastWord("") == 0)
## 一个字符
assert(solution.lengthOfLastWord("a") == 1)
## n个字符
assert(solution.lengthOfLastWord("abc") == 3)

# 一个空格
## 没有字符
assert(solution.lengthOfLastWord(" ") == 0)
## 一个字符
assert(solution.lengthOfLastWord("a ") == 1)
assert(solution.lengthOfLastWord(" b") == 1)
## n个字符
assert(solution.lengthOfLastWord("ab ") == 2)
assert(solution.lengthOfLastWord("a b") == 1)
assert(solution.lengthOfLastWord(" ab") == 2)

# 两个空格
## 没有字符
assert(solution.lengthOfLastWord("  ") == 0)
## 一个字符
assert(solution.lengthOfLastWord("a  ") == 1)
assert(solution.lengthOfLastWord(" a ") == 1)
assert(solution.lengthOfLastWord("  a") == 1)
## n个字符
assert(solution.lengthOfLastWord("abcdef  ") == 6)
assert(solution.lengthOfLastWord(" abcdef ") == 6)
assert(solution.lengthOfLastWord(" abcd ef") == 2)

# n个空格
## 没有字符
## 一个字符
## n个字符
assert(solution.lengthOfLastWord("a bc def fhij") == 4)