# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/10/17 12:17:59

# desc: 

# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。

# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 示例 :

# 给定这个链表：1->2->3->4->5

# 当 k = 2 时，应当返回: 2->1->4->3->5

# 当 k = 3 时，应当返回: 3->2->1->4->5

# 说明 :

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 边界
# k < 链表长度
# k 可能不是链表的整数倍

# 链表长度小于等于1，直接返回

# 链表长度等于2
## k<=1，不需要变化
## k=2，交换

# 链表长度等于3
## k<=1, 不需要变化
## k=2, 01交换，2不变
## k=3,全部交换


# 链表长度等于n
## k<=1, 不需要变化
## k整除： k=n/2
## k不整除： k = n/2-1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head

        lOldHead = head
        lNewHead = None
        lNewLast = None

        while lOldHead is not None:
            lTempHead = lOldHead

            bBreak = False
            for i in range(k):
                if lOldHead is not None:
                    lOldHead = lOldHead.next
                else:
                    bBreak = True
                    break
            
            if bBreak:
                break
            
            lLast = lTempHead    
            lCur = lTempHead.next
            for i in range(k-1):
                lTemp = lCur.next
                lCur.next = lLast
                lLast = lCur
                lCur = lTemp

            if lNewHead is None:
                lNewHead = lLast
            
            if lNewLast is not None:
                lNewLast.next = lLast

            lNewLast = lTempHead
            lNewLast.next = lOldHead
        
        if lNewHead is None:
            lNewHead = head

        return lNewHead
            
    
solution = Solution()

def PrintList(lhead):
    listVec = list()

    while lhead is not None:
        listVec.append(lhead.val)
        lhead = lhead.next

    print(listVec)

def PrintTestList(lhead, k):
    print(k)
    PrintList(lhead)
    PrintList(solution.reverseKGroup(lhead,k))
    print("\n")
    

def CreateList(n):
    lHead = ListNode(0)
    lCur = lHead
    for i in range(n):
        lCur.next = ListNode(i+1)
        lCur = lCur.next
    
    return lHead.next

# 链表长度小于等于1
def Test1():
    PrintTestList(CreateList(1), 0)
    PrintTestList(CreateList(1), 1)

# 链表长度等于2
def Test2():
    PrintTestList(CreateList(2), 0)
    PrintTestList(CreateList(2), 1)
    PrintTestList(CreateList(2), 2)

# 链表长度等于3
def Test3():
    PrintTestList(CreateList(3), 0)
    PrintTestList(CreateList(3), 1)
    PrintTestList(CreateList(3), 2)
    PrintTestList(CreateList(3), 3)

# 链表长度等于n
def TestN():
    for i in range(7):
        PrintTestList(CreateList(6), i)


# 给定这个链表：1->2->3->4->5

# 当 k = 2 时，应当返回: 2->1->4->3->5

# 当 k = 3 时，应当返回: 3->2->1->4->5
Test1()
Test2()
Test3()
TestN()
# PrintTestList(CreateList(6), 2)