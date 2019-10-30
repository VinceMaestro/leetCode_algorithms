from addTwoNumbers import ListNode, Solution

class Msg:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'

    def p_msg(self, type, msg):
        div = ''
        if type == "header":
            div = self.HEADER
        if type == "ok":
            div = self.OKGREEN
        if type == "warning":
            div = self.WARNING
        if type == "fail":
            div = self.FAIL
        print div + msg + self.ENDC

class Tester:
    def __init__(self):
        self.solution = Solution()
        self.msg = Msg()

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
            return(res)
        else:
            return("Null")

    def test(self, n1, n2, expectedResult, testName):
        l1 = self.createListNode(n1 if n1 >= 0 else -n1)
        l2 = self.createListNode(n2 if n2 >= 0 else -n2)
        neg =  0
        if (n1 < 0):
            neg = 1
            l1.val *= -1
        if (n2 < 0):
            neg = 1
            l2.val *= -1
        self.msg.p_msg("info", "testing : {}".format(testName))
        if neg:
            self.msg.p_msg("warning", "  (W: At least one value is negative, the program is not mean to properly work with negative)")
        l3 = self.solution.addTwoNumbers(l1, l2)
        result = self.loadResult(l3)
        if (result == expectedResult):
            self.msg.p_msg("ok", "    Result : OK")
        else:
            self.msg.p_msg("fail", "    Result : KO : Expected\t: {}\n\t\t  Got\t\t: {}".format(expectedResult, result))


    def nonNumberTest(self, ptr1, ptr2, expectedResult, testName):
        print("testing : {} : adding {} and {}".format(testName, ptr1, ptr2))
        l3 = self.solution.addTwoNumbers(ptr1, ptr2)
        result = l3
        if (result == expectedResult):
            self.msg.p_msg("ok", "    Result : OK")
        else:
            self.msg.p_msg("fail", "    Result : KO : Expected\t: {}\n\t\t  Got\t\t: {}".format(expectedResult, result))

msg = Msg()
msg.p_msg("header", "Testing addTwoNumbers")
tester = Tester()
tester.test(0, 0, 0, "simple case 1")
tester.test(1, 123, 124, "simple case 2")
tester.test(2147483647, 1, 2147483648, "max int + 1")
tester.test(2147483647, 2147483647, 4294967294, "max int *2")
tester.test(21474836472147483647214748364721474836472147483647, 21474836472147483647214748364721474836472147483647, 21474836472147483647214748364721474836472147483647+21474836472147483647214748364721474836472147483647, "Large numbers")
tester.test(99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999+99999999999999999999999999999999999999999999999999, "Large numbers")

tester.test(-1, 123, 122,"negative crashTest 1")
tester.test(-1, -123, -124,"negative crashTest 2")
tester.test(-1, 1, 0, "negative crashTest 3")
tester.test(-1, 10, 9, "negative crashTest 4")
