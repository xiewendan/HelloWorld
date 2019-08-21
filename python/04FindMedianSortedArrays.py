# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/08/20 11:58:19

# desc: desc

import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nL1Length, nL2Length = len(nums1), len(nums2)
        nL1Left, nL1Right = 0, nL1Length - 1
        nL2Left, nL2Right = 0, nL2Length - 1

        while(nL1Left < nL1Right):
            nL1Middle = math.floor((nL1Left + nL1Right)/2)
            nL1MiddleValue = nums1[nL1Middle]
            
            
            nL2Middle = math.floor((nL2Left+nL2Right/2))
            nL2MiddleValue = nums2[nL2Middle]
            


        return 1.0

    def findMaxSmallerThanValueInSortedArray(self, nums1, nLeft, nRight, nValue):
        



solutionObj = Solution()
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