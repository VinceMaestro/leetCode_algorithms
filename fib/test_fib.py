from fib import Solution

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

    def test(self, data1, expectedResult, testName):
      self.msg.p_msg("info", "testing : {}".format(testName))
      result = self.solution.fib(data1)
      if (result == expectedResult):
          self.msg.p_msg("ok", "    Result : OK")
      else:
          self.msg.p_msg("fail", "    Result : KO : Expected\t: {}\n\t\t  Got\t\t: {}".format(expectedResult, result))

msg = Msg()
msg.p_msg("header", "Testing fib")
tester = Tester()


tester.test(0, 0, "simple test 1")
tester.test(1, 1, "simple test 1")
tester.test(2, 1, "simple test 2")
tester.test(3, 2, "simple test 3")
tester.test(4, 3, "simple test 4")
tester.test(5, 5, "simple test 5")
tester.test(6, 8, "simple test 6")
tester.test(7, 13, "simple test 7")
tester.test(8, 21, "simple test 8")
tester.test(9, 34, "simple test 9")
tester.test(10, 55, "simple test 10")
tester.test(11, 89, "simple test 11")
tester.test(12, 144, "simple test 12")
tester.test(13, 233, "simple test 13")
tester.test(14, 377, "simple test 14")
tester.test(15, 610, "simple test 15")
tester.test(16, 987, "simple test 16")
tester.test(17, 1597, "simple test 17")
tester.test(18, 2584, "simple test 18")
tester.test(19, 4181, "simple test 19")
tester.test(20, 6765, "simple test 20")
tester.test(21, 10946, "simple test 21")
tester.test(22, 17711, "simple test 22")
tester.test(23, 28657, "simple test 23")
tester.test(24, 46368, "simple test 24")
tester.test(25, 75025, "simple test 25")
tester.test(26, 121393, "simple test 26")
tester.test(27, 196418, "simple test 27")
tester.test(28, 317811, "simple test 28")
tester.test(29, 514229, "simple test 29")
tester.test(30, 832040, "simple test 30")
