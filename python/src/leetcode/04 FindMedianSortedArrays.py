# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/08/20 11:58:19

# desc: 
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。
# 示例 1:

# nums1 = [1, 3]
# nums2 = [2]

# 则中位数是 2.0
# 示例 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# 则中位数是 (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            nums1, nums2 = nums2, nums1     # 确保第一个数组始终是非空的

        if len(nums1) == 0:                 # 两个数组都是空，是有问题的
            assert False

        nL1Length, nL2Length = len(nums1), len(nums2)
        nL1Left, nL1Right = 0, nL1Length - 1
        nL2Left, nL2Right = 0, nL2Length - 1

        nL3Length = nL1Length + nL2Length
        nL3Middle = (nL3Length-1) >> 1

        nL1Middle = 0
        nL2Current = 0
        nL3Current = 0

        while(nL1Left <= nL1Right):
            nL1Middle = (nL1Left + nL1Right) >> 1
            nL1MiddleValue = nums1[nL1Middle]

            nLeft, nRight = nL2Left, nL2Right
            while nLeft <= nRight:
                nMiddle = (nLeft + nRight) >> 1
                if nums2[nMiddle] < nL1MiddleValue:
                    nLeft = nMiddle + 1
                else:
                    nRight = nMiddle - 1
            nL2Current = nRight

            nL3Current = nL1Middle + nL2Current + 1
            if nL3Current < nL3Middle:
                nL1Left = nL1Middle + 1
                nL2Left = nL2Current + 1

            elif nL3Current == nL3Middle:
                # 目标点：
                nL1Left, nL1Right = nL1Middle, nL1Middle
                break
                # nL2Left, nL2Right = nL2Current + 1

            else:
                nL1Right = nL1Middle - 1
                nL2Right = nL2Current

        if nL1Left == nL1Right:      # 在第一个数组中找到
            if nL3Length % 2 == 1:   # 奇数，只找一个
                return nums1[nL1Middle]
            else:                    # 偶数，需要找到另一个，在第一个比自己大的数，可能是第二列比自己大的数
                if nL1Middle == nL1Length - 1:    # 
                    return (nums1[nL1Middle] + nums2[nL2Current+1])/2
                elif nL2Current == nL2Length - 1:
                    return (nums1[nL1Middle] + nums1[nL1Middle+1])/2
                else:
                    if nums1[nL1Middle+1] < nums2[nL2Current+1]:
                        return (nums1[nL1Middle] + nums1[nL1Middle+1])/2
                    else:
                        return (nums1[nL1Middle] + nums2[nL2Current+1])/2


        else:                       # 第一个数在第二个数组中
            if nL1Middle == nL1Left:
                nL2Middle = nL2Right - (nL3Current - 1- nL3Middle)
                if nL3Length % 2 == 1:   # 奇数，只找一个
                    return nums2[nL2Middle]
                else:
                    if nL2Middle == nL2Length - 1:
                        return (nums2[nL2Middle] + nums1[nL1Middle]) / 2
                    else:
                        if nums2[nL2Middle+1] < nums1[nL1Middle]:
                            return (nums2[nL2Middle] + nums2[nL2Middle+1]) / 2
                        else:
                            return (nums2[nL2Middle] + nums1[nL1Middle]) / 2
            
            else:
                nL2Middle = nL2Left + (nL3Middle - (nL3Current + 1))
                if nL3Length %2 == 1:    # 奇数，只找一个
                    return nums2[nL2Middle]
                else:
                    if nL2Middle == nL2Length - 1:
                        return (nums2[nL2Middle] + nums1[nL1Middle + 1])/2
                    elif nL1Middle == nL1Length - 1:
                        return (nums2[nL2Middle] + nums2[nL2Middle + 1]) / 2
                    else:
                        if nums2[nL2Middle + 1] < nums1[nL1Middle+1]:
                            return (nums2[nL2Middle] + nums2[nL2Middle + 1]) / 2
                        else:
                            return (nums2[nL2Middle] + nums1[nL1Middle + 1])/2

    def findMaxSmallerThanValueInSortedArray(self, nums, nLeft, nRight, nValue):
        while nLeft <= nRight:
            nMiddle = (nLeft + nRight)//2
            if nums[nMiddle] < nValue:
                nLeft = nMiddle + 1
            else:
                nRight = nMiddle - 1
        
        return nRight


solutionObj = Solution()
import math
assert(math.isclose(solutionObj.findMedianSortedArrays([0], []), 0))
assert(math.isclose(solutionObj.findMedianSortedArrays([], [0]), 0))
assert(math.isclose(solutionObj.findMedianSortedArrays([0,1], []), 0.5))
assert(math.isclose(solutionObj.findMedianSortedArrays([], [0,1]), 0.5))

assert(math.isclose(solutionObj.findMedianSortedArrays([0,1,2], []), 1.0))

assert(math.isclose(solutionObj.findMedianSortedArrays([0], [1]), 0.5))
assert(math.isclose(solutionObj.findMedianSortedArrays([1,2,3], [0]), 1.5))
assert(math.isclose(solutionObj.findMedianSortedArrays([1,5,10], [2,3,4]), 3.5))
assert(math.isclose(solutionObj.findMedianSortedArrays([1,3], [2]), 2))
assert(math.isclose(solutionObj.findMedianSortedArrays([1,2], [3,4]), 2.5))

print((1+2)>>1)
print((1+2)/2)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m>n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin = 0
        imax = m
        halflen = (m+n+1)//2
        while imin<=imax:
            i = (imin + imax)//2
            j = halflen - i
            if i<m and nums1[i]<nums2[j-1]:
                imin += 1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax -= 1
            else:
                if i==0:
                    max_left = nums2[j-1]
                elif j==0:
                    max_left = nums1[i-1]
                else:
                    max_left = max([nums1[i-1], nums2[j-1]])
                if (m+n)%2==1:
                    return max_left
                if i==m:
                    min_right = nums2[j]
                elif j==n:
                    min_right = nums1[i]
                else:
                    min_right = min([nums1[i], nums2[j]])
                return (max_left+min_right)/2.0