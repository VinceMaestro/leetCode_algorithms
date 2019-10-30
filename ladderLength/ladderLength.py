        # On veut savoir si beginWord est connecte a endWord et si oui, la distance qui les separe
        #
        # append beginWord dans la queue
        # distFromBegin = {beginWord: 0}
        # while (queue)
        #     wordToCompare = remove(first from queue)
        #     on retire wordToCompare de copyList
            # partir de wordToCompare comparer a chaque mot dans copyList
                # si il a une seule diff alors il est voisin
                #     distFromBegin.append(mot: distFromBegin[wordToCompare] + 1)
                #     si le voisin est le endWord on retrourne la wordDistFromStart[mot]
                #     sinon on append le voisin dans la queue



class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if ((type(beginWord) is not str) or (beginWord == "") or (type(endWord) is not str) or (endWord == "") or (type(wordList) is not list) or (wordList == []) or (endWord not in wordList)):
            return(0)
        queue = []
        w_len = len(beginWord)
        queue.append(beginWord)
        distFromBegin = {beginWord: 1}
        copyList = [word for word in wordList]
        if (beginWord in copyList):
            copyList.remove(beginWord)

        while (queue):
            newList = []
            word = queue.pop(0)
            for w in copyList:
                diff = 0
                i = 0
                while (i < w_len and diff <= 1):
                    if word[i] != w[i]:
                        diff += 1
                    i += 1
                if (diff > 1):
                    newList.append(w)
                elif (diff == 1):
                    distFromBegin[w] = distFromBegin[word] + 1
                    queue.append(w)
                    if (w == endWord):
                        return(distFromBegin[w])
            copyList = newList
        return(0)
