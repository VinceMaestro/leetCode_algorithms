from x import Solution

class Tester:
    def __init__(self):
        self.solution = Solution()

    def test(self, data1, data2, testName):
      print("testing : {} : with {} and {}".format(testName, data1, data2))
      result = self.solution.function(data1, data2)
      print("    Result : {}".format(result))


tester = Tester()
tester.test(data1, data2, "testName")
