# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/12/25 22:49:21

# desc: desc

# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/min-stack
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.m_nCount = 0
        self.m_listStack = []

        self.m_nMinCount = 0
        self.m_listMinStack = []
        

    def pushMin(self, x: int, index: int) -> None:
        if self.m_nMinCount == 0:
            self.m_nMinCount += 1
            self.m_listMinStack.append(0)
        elif self.m_nMinCount > 0:
            nMinIndex = self.m_listMinStack[self.m_nMinCount-1]
            if x < self.m_listStack[nMinIndex]:
                self.m_nMinCount += 1
                self.m_listMinStack.append(index)
        else:
            pass
    
    def popMin(self, index: int) -> None:
        if self.m_nMinCount <= 0:
            return None
        
        nMinIndex = self.m_listMinStack[self.m_nMinCount-1]
        if nMinIndex >= index:
            self.m_listMinStack.pop()
            self.m_nMinCount -= 1
            return nMinIndex
        else:
            return nMinIndex
        

    def push(self, x: int) -> None:
        self.m_nCount += 1
        self.m_listStack.append(x)
        self.pushMin(x, self.m_nCount-1)

    def pop(self) -> None:
        if self.m_nCount > 0:
            self.popMin(self.m_nCount-1)
            self.m_nCount -= 1
            return self.m_listStack.pop()
        else:
            return None

    def top(self) -> int:
        if self.m_nCount > 0:
            return self.m_listStack[self.m_nCount-1]
        else:
            return None
        

    def getMin(self) -> int:
        if self.m_nMinCount <= 0:
            return None
        
        nMinIndex = self.m_listMinStack[self.m_nMinCount-1]
        return self.m_listStack[nMinIndex]
        


# Your MinStack object will be instantiated and called as such:
# 思路
# 第一个数组用来存储数据，实现数据栈
# 第二个数组存储最小值得栈，

# 代码
    
# 边界
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)
assert(minStack.getMin() == -2)
minStack.pop()
assert(minStack.getMin() == -2)