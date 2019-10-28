class Solution:
    def compare_str(self, first, last):
        firstTmp = first
        lastTmp = last
        while (firstTmp < lastTmp and self.str[firstTmp] == self.str[lastTmp]):
            firstTmp += 1
            lastTmp -= 1
        if (firstTmp >= lastTmp):
            return last - first
        else:
            return 0

    def longestPalindrome(self, s):
        if (s):
            self.str = s
            iFirstPtrFinal = 0
            iLastPtrFinal = 0
            iFirstPtrTmp = 0
            while (iFirstPtrTmp < len(self.str) and (iLastPtrFinal - iFirstPtrFinal != len(self.str) - 1)):
                iLastPtrTmp = len(self.str) - 1
                while (iLastPtrTmp > iFirstPtrTmp):
                    if (self.compare_str(iFirstPtrTmp, iLastPtrTmp) > iLastPtrFinal - iFirstPtrFinal):
                        iLastPtrFinal = iLastPtrTmp
                        iFirstPtrFinal = iFirstPtrTmp
                    iLastPtrTmp -= 1
                iFirstPtrTmp += 1
            ret = ""
            while (iFirstPtrFinal <= iLastPtrFinal):
                ret += self.str[iFirstPtrFinal]
                iFirstPtrFinal += 1
            return ret
        else:
            return s
