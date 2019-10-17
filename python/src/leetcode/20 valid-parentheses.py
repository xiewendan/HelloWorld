# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/09/27 22:19:09

# desc: 
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class StackCls(object):
    def __init__(self):
        self.m_listObj = []
        self.m_nCount = 0
    
    def Push(self, obj):
        self.m_nCount += 1
        self.m_listObj.append(obj)

    def Pop(self):
        if self.m_nCount <= 0:
            return None
        self.m_nCount -= 1
        return self.m_listObj.pop()


class Solution:
    def isValid(self, s):
        stackObj = StackCls()
        dictLeft = {"(":")", "[":"]", "{":"}"}
        dictRight = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in dictLeft:
                stackObj.Push(char)
            elif char in dictRight:
                charPop = stackObj.Pop()
                if dictRight[char] != charPop:
                    return False
            else:
                return False
        
        return stackObj.Pop() is None

solutionObj = Solution()
# 空串
assert(solutionObj.isValid(""))# 0
# 成对，嵌套
assert(solutionObj.isValid("{[()()][]}"))# 0
# 不成对
assert(solutionObj.isValid("{") == False)# 0
assert(solutionObj.isValid("}") == False)# 0