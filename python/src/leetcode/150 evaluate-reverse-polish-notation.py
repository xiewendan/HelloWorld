# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/12/28 15:01:19

# desc: desc

# 根据逆波兰表示法，求表达式的值。

# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

# 说明：

# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 示例 1：

# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
# 示例 2：

# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: (4 + (13 / 5)) = 6
# 示例 3：

# 输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 输出: 22
# 解释: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# 利用stack的机制

# 代码
class Solution:
    def evalRPN(self, tokens) -> int:

        listStack = [0] # 哨兵

        dictAction = {
            '+':lambda a,b:a+b,
            '-':lambda a,b:a-b,
            '*':lambda a,b:a*b,
            '/':lambda a,b:a/b
        }

        for ValueData in tokens:
            if ValueData in dictAction:
                listStack[-2] = int(dictAction[ValueData](listStack[-2],listStack[-1]))
                listStack.pop()
            else:
                listStack.append(int(ValueData))
        
        return listStack.pop()


# 边界
solution = Solution()

# 0个符号
assert(solution.evalRPN([]) == 0)

# 1个符号
assert(solution.evalRPN(["2", "1", "+"]) == 3)
assert(solution.evalRPN(["2", "1", "-"]) == 1)
assert(solution.evalRPN(["2", "1", "*"]) == 2)
assert(solution.evalRPN(["4", "2", "/"]) == 2)

# 2个符号
assert(solution.evalRPN(["2", "1", "+", "3", "*"]) == 9)
assert(solution.evalRPN(["4", "13", "5", "/", "+"]) == 6)

# n个符号
assert(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22)