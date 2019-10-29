class Solution:
    def initHashMap(self):
        letter = 0
        while (letter <= 255):
            self.hashMap[chr(letter)] = -1
            letter += 1

    def lengthOfLongestSubstring(self, s):
        if (not s or type(s) is not str):
            return(0)
        self.hashMap = {}
        self.initHashMap()
        longest = 0
        length = 0
        i = 0
        min = 0
        max = len(s)
        while (s and i < max):
            if (self.hashMap[s[i]] < min):
                length += 1
            else:
                length = i - self.hashMap[s[i]]
                min = self.hashMap[s[i]]
            longest = length if (length > longest) else longest
            self.hashMap[s[i]] = i
            i += 1
        return longest
