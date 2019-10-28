from addTwoNumbers import ListNode, Solution

def createListNode(nbr):
    list = ListNode(nbr % 10)
    ptr = list
    tmp = nbr / 10
    while (tmp % 10 != tmp or tmp != 0):
        list.next = ListNode(tmp % 10)
        tmp = tmp / 10
        list = list.next
    return ptr

def print_list(list):
    while (list):
        print(list.val)
        list = list.next

sol = Solution()
l1 = createListNode(123)
l2 = createListNode(1)
l3 = sol.addTwoNumbers(l1, l2)
print_list(l3)
