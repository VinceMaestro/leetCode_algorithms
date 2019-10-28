class Solution:
    def __init__(self):
        self.matrix = []
        self.iMin = 0
        self.jMax = 0

    def initMatrix(self, lenght):
        for i in range(0, lenght):
            self.matrix.append([])
            for j in range(0, lenght):
                if (i == j):
                    self.matrix[i].append(True)
                elif ((j == i + 1) and (self.str[i] == self.str[j])):
                    self.matrix[i].append(True)
                    if (j - i > self.jMax - self.iMin):
                        self.jMax = j
                        self.iMin = i
                else:
                    self.matrix[i].append(False)

    def findAllPalindromes(self, lenght):
        offset = 2
        i = 0
        j = offset
        while (i < lenght - offset or j < lenght):
            if (j >= i):
                if (self.matrix[i + 1][j - 1] == True and self.str[i] == self.str[j]):
                    self.matrix[i][j] = True
                    if (j - i > self.jMax - self.iMin):
                        self.jMax = j
                        self.iMin = i
                else:
                    self.matrix[i][j] = False
            i += 1
            j += 1
            if (j == lenght and i == lenght - offset):
                offset += 1
                j = offset
                i = 0

    def longestPalindrome(self, s):
        if (s and s != s[::-1]):
            self.str = s
            lenght = len(self.str)
            self.initMatrix(lenght)
            self.findAllPalindromes(lenght)
            longest = s[self.iMin: self.jMax + 1]
            return(longest)
        else:
            return(s)
