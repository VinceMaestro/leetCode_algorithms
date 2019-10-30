class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if ((type(beginWord) is not str) or (beginWord == "") or (type(endWord) is not str) or (endWord == "") or (type(wordList) is not list) or (wordList == []) or (endWord not in wordList)):
            return(0)
        w_len = len(beginWord)
        neighborsTab = {}
        regexTab = {}
        wordList.append(beginWord)
        for word in wordList:
            i = 0
            while(i < w_len):
                regex = word[:i] + '*' + word[i+1:]
                if (regex in neighborsTab):
                    neighborsTab[regex].append(word)
                else:
                    neighborsTab[regex] = [word]
                if (word in regexTab):
                    regexTab[word].append(regex)
                else:
                    regexTab[word] = [regex]
                i += 1
        queue = []
        queue.append(beginWord)
        distFromBegin = {beginWord: 1}
        posQueue = 0
        while (posQueue < len(queue)):
            newList = []
            refWord = queue[posQueue]
            posQueue += 1
            for regex in regexTab[refWord]:
                for neighbor in neighborsTab[regex]:
                    if neighbor != refWord:
                        if (not neighbor in distFromBegin):
                            distFromBegin[neighbor] = distFromBegin[refWord] + 1
                        if (neighbor == endWord):
                            return(distFromBegin[neighbor])
                        queue.append(neighbor)
                neighborsTab[regex] = []
        return(0)
