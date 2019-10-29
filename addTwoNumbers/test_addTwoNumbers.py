from addTwoNumbers import ListNode, Solution

class Tester:
    def __init__(self):
        self.solution = Solution()

    def createListNode(self, nbr):
        list = ListNode(nbr % 10)
        ptr = list
        tmp = nbr / 10
        while (tmp % 10 != tmp or tmp != 0):
            list.next = ListNode(tmp % 10)
            tmp = tmp / 10
            list = list.next
        return ptr

    def loadResult(self, list):
        if (list):
            i = 0
            res = 0
            while (list):
                res += list.val * (10 ** i)
                list = list.next
                i += 1
            return(str(res))
        else:
            return("Null")

    def test(self, n1, n2, testName):
        # print("Generating Nodes ...")
        l1 = self.createListNode(n1 if n1 >= 0 else -n1)
        l2 = self.createListNode(n2 if n2 >= 0 else -n2)
        neg =  0
        if (n1 < 0):
            neg = 1
            l1.val *= -1
        if (n2 < 0):
            neg = 1
            l2.val *= -1
        print("testing : {} : adding {} and {}".format(testName, n1, n2))
        if neg:
            print("  (W: At least one value is negative, the program is not mean to properly work with negative)")
        l3 = self.solution.addTwoNumbers(l1, l2)
        print("    Result : {}".format(self.loadResult(l3)))

    def nonNumberTest(self, ptr1, ptr2, testName):
        print("testing : {} : adding {} and {}".format(testName, ptr1, ptr2))
        l3 = self.solution.addTwoNumbers(ptr1, ptr2)
        print("    Result : {}".format(l3))

tester = Tester()
tester.test(1, 123, "simple case")
tester.test(-1, 123, "one negative")
tester.test(-1, -123, "two negative")
tester.test(-1, 1, "one negative border case")
tester.test(-1, 10, "one negative border case")
tester.test(2147483647, 1, "max int + 1")
tester.test(2147483647, 2147483647, "max int *2")
tester.test(0, 0, "0 + 0")
tester.test(21474836472147483647214748364721474836472147483647, 21474836472147483647214748364721474836472147483647, "Large numbers")
tester.test(99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999, "Large numbers")
