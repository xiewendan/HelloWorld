# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/11/25 22:55:28

# desc: desc

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 2 -> abc
# 3 -> def
# 4 -> ghi
# 5 -> jkl
# 6 -> mno
# 7 -> pqrs
# 8 -> tuv
# 9 -> wxyz

# 示例:

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 递归

# 代码
class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    def letterCombinations(self, digits):
        dictInt2Letter = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
        }
        nLen = len(digits)
        if nLen == 0:
            return []
        if nLen == 1:
            return dictInt2Letter[digits]
        
        subLetterRet = self.letterCombinations(digits[1:])
        letterRet = []
        for char in dictInt2Letter[digits[0]]:
            for subChar in subLetterRet:
                letterRet.append(char + subChar)
        return letterRet
    
# 边界
solution = Solution()
assert(solution.letterCombinations("2")==['a','b','c'])
assert(solution.letterCombinations("23")==["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])