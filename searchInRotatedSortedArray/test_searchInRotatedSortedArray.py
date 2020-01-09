from searchInRotatedSortedArray import Solution

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

    def test(self, data, target, expectedResult, testName):
      self.msg.p_msg("info", "testing : {}".format(testName))
      result = self.solution.search(data, target)
      if (result == expectedResult):
          self.msg.p_msg("ok", "    Result : OK")
      else:
          self.msg.p_msg("fail", "    Result : KO : Expected\t: {}\n\t\t  Got\t\t: {}".format(expectedResult, result))

msg = Msg()
msg.p_msg("header", "Testing searchInRotatedSortedArray")
tester = Tester()
tester.test([1,3,5], 4, -1, "simple case : missing number")
tester.test([3,1], 1, 1, "simple case : size 2 array")
tester.test([1,3], 1, 0, "simple case : size 2 array")
tester.test([1,3], 2, -1, "simple case : size 2 array && missing number")
tester.test([], 0, -1, "simple case : size 0 array")
tester.test([0], 0, 0, "simple case : size 1 array")
tester.test([4,5,6,7,0,1,2], 0, 4, "simple case : size 7 array")
tester.test([4,5,6,7,0,1,2], 3, -1, "simple case : size 7 array && missing number")
