# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/18 19:04:37

# desc: desc

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import sys
class Solution:
    def threeSumClosest(self, nums, target):
        nLen = len(nums)
        if nLen <= 2:
            assert(False)
        if nLen == 3:
            return nums[0] + nums[1] + nums[2]

        numsSort = nums.copy()
        numsSort.sort()

        nIndex1 = 0
        nRange1 = nLen - 2
        nLastValue = numsSort[0] - 1
        nMaxIndex = nLen - 1
        
        nRetSum = 0
        nMinAbsDelta = sys.maxsize
        while nIndex1 < nRange1:
            if numsSort[nIndex1] == nLastValue:
                nIndex1 += 1
                continue
            nLastValue = numsSort[nIndex1]

            nSum = target - nLastValue
            nLeftIndex = nIndex1 + 1
            nRightIndex = nMaxIndex

            # 当前情况的最小值，或最大值
            if numsSort[nLeftIndex] + numsSort[nLeftIndex + 1] >= nSum:
                nDelta = nSum - numsSort[nLeftIndex] - numsSort[nLeftIndex + 1]
                if nDelta == 0:
                    return target

                if abs(nDelta) < nMinAbsDelta:
                    nMinAbsDelta = abs(nDelta)
                    nRetSum = nLastValue + numsSort[nLeftIndex] + numsSort[nLeftIndex + 1]

                break

            # 当前情况的最大值
            elif numsSort[nRightIndex] + numsSort[nRightIndex - 1] <= nSum:
                nDelta = nSum - numsSort[nRightIndex] - numsSort[nRightIndex - 1]

                if nDelta == 0:
                    return target
                
                if abs(nDelta) < nMinAbsDelta:
                    nMinAbsDelta = abs(nDelta)
                    nRetSum = nLastValue + numsSort[nRightIndex] + numsSort[nRightIndex - 1]

            # 介于之间的
            else:
                while nLeftIndex < nRightIndex:
                    nDelta = nSum - numsSort[nLeftIndex] - numsSort[nRightIndex] 

                    if abs(nDelta) < nMinAbsDelta:
                        nMinAbsDelta = abs(nDelta)
                        nRetSum = nLastValue + numsSort[nLeftIndex] + numsSort[nRightIndex]

                    if nDelta == 0:
                        return nLastValue + numsSort[nLeftIndex] + numsSort[nRightIndex]
                    elif nDelta > 0:
                        nLeftIndex += 1
                    else:
                        nRightIndex -= 1

            nIndex1 += 1
        
        return nRetSum

    
solution = Solution()
def ListEqual(list1, list2):
    nLen1 = len(list1)
    nLen2 = len(list2)
    
    if nLen1 != nLen2:
        return False
    
    list1Temp = list1.copy()
    list2Temp = list2.copy()
    list1Temp.sort()
    list2Temp.sort()

    for i in range(nLen1):
        if list1Temp[i] != list2Temp[i]:
            return False
    
    return True
        
# 元素个数 <= 2, 不存在


# 元素个数 == 3, 直接返回
# [1,2,3]  任何数
assert(solution.threeSumClosest([1,2,0], 10)==3)        # [0,1,2]

# 元素个数 > 3 
## 存在元素相同
### target 正数        [-3,-2,-1, 0, 1, 2, 3, 1]   1 
assert(solution.threeSumClosest([-3, 0, -10, 2, 1, -10], 1) == 0) 
### target 负数        [-3,-2,-1, 0, 1, 2, 3, 1]   -1 
assert((solution.threeSumClosest([-3, 0, -10, 2, 1, -10], -1) == -1)) 
### target 0           [-3,-2,-1, 0, 1, 2, 3, 1]   0
assert((solution.threeSumClosest([-10, -3, 0, 1, 2, -10], 0) == 0)) 

## 都是不同元素
### target 正数        [-3,-2,-1, 0, 1, 2, 3]   1 
assert((solution.threeSumClosest([-3, 0, 1, 2, -10], 0) == 0)) 
### target 负数        [-3,-2,-1, 0, 1, 2, 3]   -1 
assert((solution.threeSumClosest([-3, 0, 2, 1, -10], -1) == -1)) 
### target 0           [-3,-2,-1, 0, 1, 2, 3]   0
assert((solution.threeSumClosest([-3, 0, 1, 2, -10], 0) == 0)) 
print(solution.threeSumClosest([-3, 0, 1, 2, -10], 0))



# 当前情况大于，直接返回
assert((solution.threeSumClosest([-3, 0, 1, 2, -10], 0) == 0)) 

# 最小情况大于，直接返回
assert((solution.threeSumClosest([-3, 0, 1, 2, -10], -13) == -13)) 
assert((solution.threeSumClosest([-3, 0, 1, 2, -10], -100) == -13)) 

# 最大值大于
assert((solution.threeSumClosest([-3, 0, 1, 2, -10], 3) == 3)) 
assert((solution.threeSumClosest([-3, 0, 1, 2, -10], -7) == -7)) 