from x import Solution

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

    def test(self, data1, data2, expectedResult, testName):
      self.msg.p_msg("info", "testing : {}".format(testName))
      result = self.solution.function(data1, data2)
      if (result == expectedResult):
          self.msg.p_msg("ok", "    Result : OK")
      else:
          self.msg.p_msg("fail", "    Result : KO : Expected\t: {}\n\t\t  Got\t\t: {}".format(expectedResult, result))

msg = Msg()
msg.p_msg("header", "Testing functionName")
tester = Tester()
tester.test(data1, data2, expectedResult, "testName")
