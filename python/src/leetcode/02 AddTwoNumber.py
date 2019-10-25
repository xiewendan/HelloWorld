# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/08/16 23:16:19

# desc: HelloWorld.py
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lh = ListNode(0)
        lc = lh
        nAddEx = 0
        while(l1 and l2):
            nVal = l1.val + l2.val + nAddEx
            if(nVal < 10):
                nAddEx = 0
            else:
                nAddEx = 1
                nVal = nVal - 10
                
            lt = ListNode(nVal)

            lc.next = lt
            lc = lt

            l1 = l1.next
            l2 = l2.next

        ll = l1
        if l1 is None:
            ll = l2

        while(ll):
            nVal = ll.val + nAddEx
            if(nVal < 10):
                nAddEx = 0
                lt = ListNode(nVal)
                lc.next = lt
                lc = lt
                lc.next = ll.next
                break

            else:
                nAddEx = 1
                nVal = nVal - 10

            lt = ListNode(nVal)

            lc.next = lt
            lc = lt

            ll = ll.next
        
        if nAddEx > 0:
            lc.next = ListNode(nAddEx)

        return lh.next

        
l1 = ListNode(1)
lc = l1
lc.next = ListNode(8)
# lc = lc.next
# lc.next = ListNode(5)

l2 = ListNode(0)
# lc = l2
# lc.next = ListNode(6)
# lc = lc.next
# lc.next = ListNode(4)

solution = Solution()
lh = solution.addTwoNumbers(l1, l2)

while(lh):
    print(lh.val)
    lh = lh.next


