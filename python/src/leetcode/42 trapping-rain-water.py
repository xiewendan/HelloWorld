# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/10 12:31:40

# desc: 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class MinMaxPair(object):
    def __init__(self, nMin, nMax):
        assert(0 <= nMin < nMax)
        self.m_nMin = nMin
        self.m_nMax = nMax
    
    def Include(self, onePair):
        return self.Min() <= onePair.Min() and onePair.Max() <= self.Max()
    
    def Min(self):
        return self.m_nMin
    
    def Max(self):
        return self.m_nMax

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
    
    def Last(self):
        if self.m_nCount > 0:
            return self.m_listObj[self.m_nCount]
        return None
    
    def IsEmpty(self):
        return self.m_nCount == 0
        

class Solution:
    def trap(self, height):
        nLen = len(height)
        if nLen < 3:
            return 0
        
        indexStackObj = StackCls()
        indexPairStackObj = StackCls()
        for nCurIndex in range(nLen):
            nCurHeight = height[nCurIndex]

            nLeftIndex = None
            while not indexStackObj.IsEmpty():
                nPreIndex = indexStackObj.Pop()
                nPreHeight = height[nPreIndex]
                
                if nCurHeight < nPreHeight:
                    nLeftIndex = nPreIndex
                    indexStackObj.Push(nPreIndex)
                    break
                elif nCurHeight == nPreHeight:
                    nLeftIndex = nPreIndex
                    break
                else:
                    nLeftIndex = nPreIndex
            
            indexStackObj.Push(nCurIndex)

            if nLeftIndex is None:
                pass
            elif nCurIndex - nLeftIndex <= 1:
                pass
            else:
                newPair = MinMaxPair(nLeftIndex, nCurIndex)
                while not indexPairStackObj.IsEmpty():
                    oldPair = indexPairStackObj.Pop()
                    if newPair.Include(oldPair):
                        pass
                    else:
                        indexPairStackObj.Push(oldPair)
                        break
                indexPairStackObj.Push(newPair)
            
        
        nSum = 0
        while not indexPairStackObj.IsEmpty():
            indexPair = indexPairStackObj.Pop()
            nMin = indexPair.Min()
            nMax = indexPair.Max()
            nMinHeight = min(height[nMin], height[nMax])
            for nIndex in range(nMin, nMax):
                nSum += max(nMinHeight - height[nIndex],0)
        
        return nSum
