# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/09/10 22:15:33

# desc: 字符串转整数
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。

# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

# 在任何情况下，若函数不能进行有效的转换时，请返回 0。

# 说明：

# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-to-integer-atoi
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 测试：
# 1、开头为空格和非空格：  1，1   ==> 1，1
# 2、开头为符号：+1a，-10a, 10      ==> 1, -10, 10
# 3、非法开头：a100             ==> 0
# 4、超出范围：小于 -pow(2,31), 大于 pow(2,31)-1 ==>INT_MAX, INT_MIN

INT_MAX = pow(2,31) -1
INT_MIN = -pow(2,31)
class Solution:
    def myAtoi(self, szStr: str) -> int:
        nIndex = 1
        szStr = szStr.strip()
        if len(szStr) == 0:
            return 0
        nChar = szStr[0]
        if not nChar.isdigit() and nChar != "+" and nChar != "-":
            return 0

        nSign = 1
        if nChar == "+":
            szStr = szStr[1:]
            pass
        elif nChar == "-":
            szStr = szStr[1:]
            nSign = -1
        else:
            pass
        
        if len(szStr) == 0:
            return 0

        nChar = szStr[0]
        if not nChar.isdigit():
            return 0

        nEnd = 0 
        bHasPoint = False
        for char in szStr:
            if char.isdigit():
                nEnd += 1
            else:
                break
        
        nSum = nSign * int(szStr[:nEnd])

        if nSum > INT_MAX:
            return INT_MAX
        elif nSum < INT_MIN:
            return INT_MIN
        else:
            return nSum

solutionObj = Solution()
assert(solutionObj.myAtoi("   1") == 1)# 0
assert(solutionObj.myAtoi("   1.1") == 1)# 0
assert(solutionObj.myAtoi("1") == 1)# 0
assert(solutionObj.myAtoi("3.1415") == 3)# 0
assert(solutionObj.myAtoi("01") == 1)# 0
assert(solutionObj.myAtoi("12345601") == 12345601)# 0

assert(solutionObj.myAtoi("+1a") == 1)# 0
assert(solutionObj.myAtoi("-10a") == -10)# 0

assert(solutionObj.myAtoi("a100") == 0)# 0

assert(solutionObj.myAtoi("1234567890123") == INT_MAX)# 0
assert(solutionObj.myAtoi("-1234567890123") == INT_MIN)# 0
import math
print(math.sqrt(pow(1.34,2) + pow(2.33,2)))
print('.'.isdigit())
print("123"[:2])
