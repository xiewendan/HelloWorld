# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/09/26 12:56:23

# desc: desc

# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:

# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/plus-one
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        nLen = len(digits)

        nAdd = 1
        for i in range(nLen-1,-1,-1):
            digits[i] = digits[i] + nAdd
            if digits[i] > 9:
                digits[i] = digits[i] - 10
            else:
                return digits

        digitsNew = [1]
        digitsNew.extend(digits)
        return digitsNew


solution = Solution()
def CompareList(vecList1, vecList2):
    # 长度一样，每个元素一样
    nLenList1 = len(vecList1)
    if nLenList1 != len(vecList2):
        return False
    
    for i in range(nLenList1):
        if vecList1[i] != vecList2[i]:
            return False
    
    return True


# 个位数：0, 1, 9
# 两位数：10,19,99
assert(CompareList([1], solution.plusOne([0]))) 
assert(CompareList([2], solution.plusOne([1]))) 
assert(CompareList([1,0], solution.plusOne([9]))) 
assert(CompareList([1,1], solution.plusOne([1,0]))) 
assert(CompareList([2,0], solution.plusOne([1,9]))) 
assert(CompareList([1,0,0], solution.plusOne([9,9]))) 

