# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/08/26 12:21:20

# desc: 
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true
# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x!=0):
            return False
        nReverse = 0
        while x > nReverse:
            nReverse = nReverse * 10 + x % 10
            x = x // 10
        
        return nReverse == x  or nReverse // 10 == x

import time
nStart = time.time()

solution = Solution()
for i in range(1, 1000):
    assert(solution.isPalindrome(0))
    assert(solution.isPalindrome(1))
    assert(solution.isPalindrome(-1) == False)
    assert(solution.isPalindrome(22))
    assert(solution.isPalindrome(10) == False)
    assert(solution.isPalindrome(121))
    assert(solution.isPalindrome(-121) == False)

nEnd = time.time()
nEscape = nEnd - nStart
print(nEscape * 1000)