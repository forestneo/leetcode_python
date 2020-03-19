# -*- coding: utf-8 -*-
# @Time    : 2020/3/16
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 002.py
# @Software: PyCharm
# @Function: 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        print("%d" % self.val, end="")
        a = self.next
        while a is not None:
            print("%d" % a.val, end="")
            a = a.next
        print("")

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

def myadd(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)
    tmp = head
    plus = 0
    while l1 is not None and l2 is not None:
        new_node = ListNode((l1.val + l2.val + plus) % 10)
        plus = int((l1.val + l2.val + plus) / 10)
        tmp.next = new_node
        l1 = l1.next
        l2 = l2.next
        print(new_node.val)
        tmp = tmp.next
    lst = l1 if l2 is None else l2

    if l1 is None and l2 is None and plus != 0:
        new_node = ListNode(plus)
        tmp.next = new_node
        return head.next

    while lst is not None:
        new_node = ListNode((lst.val + plus) % 10)
        plus = int((lst.val + plus) / 10)
        tmp.next = new_node
        lst = lst.next
        print(new_node.val)
        tmp = tmp.next
    if plus != 0:
        new_node = ListNode(plus)
        tmp.next = new_node
    return head.next



if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    b.next = a
    c = ListNode(2)
    c.next = b
    data1 = c

    a = ListNode(4)
    b = ListNode(6)
    b.next = a
    c = ListNode(5)
    c.next = b

    data2 = c
    data1.print()
    data2.print()

    res = myadd(data1, data2)
    res.print()
    pass