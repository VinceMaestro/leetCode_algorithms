from longestSubstringWithoutRepeatingCharacters import Solution

class Tester:
    def __init__(self):
        self.solution = Solution()

    def test(self, data, testName):
      print("testing : {} : with {}".format(testName, data))
      result = self.solution.lengthOfLongestSubstring(data)
      print("    Result : {}".format(result))


tester = Tester()
tester.test("abba", "simple case")
tester.test("dvdf", "simple case")
tester.test(" ", "simple case")
tester.test("bbbbbb", "simple case")
tester.test("pwwkew", "simple case")
tester.test("pwkewtpwkewupwkewipwkewjpwkewppwkewm", "simple case")
tester.test("azertyuiopqsdfghjklmwxcvbn", "simple case")
tester.test("pwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwkewppwkewmpwkewtpwkewupwkewipwkewjpwk", "long str")
tester.test("\t\f\n", "invisible char")
tester.test(1, "int")
s = "string"
tester.test(s[0], "char")
s = ""
for i in range (0, 256):
    s = s + chr(i)
tester.test(s, "All ASCII")
