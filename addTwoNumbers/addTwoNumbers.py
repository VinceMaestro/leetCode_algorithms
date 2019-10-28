class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        newList = ListNode(0)
        node = newList
        while (l1 or l2):
            node.val += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if (l1 or l2 or node.val >= 10):
                i = 0
                if (node.val >= 10) :
                    i += 1
                    node.val -= 10
                node.next = ListNode(i)
                node = node.next
        return newList
