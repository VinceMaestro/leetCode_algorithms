class Solution:
    def __init__(self):
        self.visited = []
        self.nodeLookupById = {}
        self.non_visited = []
        self.connectedToExt = 0
        self.toFlip = []
        self.stack = []

    def newNode(self, id, i, j):
        node = {"id": id, "i": i, "j": j, "neighbor": []}
        self.nodeLookupById[id] = node
        self.idLookupByIndex[i][j] = id
        self.non_visited.append(id)
        return (node)

    def lookForAdjacentAndConnect(self, id, i, j):
        neighborId = -1
        if (i > 0):
            neighborId = self.idLookupByIndex[i - 1][j]
            if (neighborId > -1):
                self.nodeLookupById[id]["neighbor"].append(self.nodeLookupById[neighborId])
                self.nodeLookupById[neighborId]["neighbor"].append(self.nodeLookupById[id])
        if (j > 0):
            neighborId = self.idLookupByIndex[i][j - 1]
            if (neighborId > -1):
                self.nodeLookupById[id]["neighbor"].append(self.nodeLookupById[neighborId])
                self.nodeLookupById[neighborId]["neighbor"].append(self.nodeLookupById[id])

    def createRegionsGraph(self, board):
        id = 0
        for i in range(0, self.iLen):
            for j in range(0, self.jLen):
                if (board[i][j] == "O"):
                    node = self.newNode(id, i, j)
                    self.lookForAdjacentAndConnect(id, i, j)
                    id += 1
        self.maxId = id - 1

    def findSurroundedRegions(self, id):
        self.stack.append(id)
        while (self.non_visited != [] or self.stack != []):
            id = self.stack.pop()
            while (id in self.visited and self.stack != []):
                id = self.stack.pop()
            if (not id in self.visited):
                self.visited.append(id)
                self.non_visited.remove(id)
                if (self.connectedToExt == 0 and ((self.nodeLookupById[id]["i"] == 0) or (self.nodeLookupById[id]["i"] == self.iLen - 1) or (self.nodeLookupById[id]["j"] == 0) or (self.nodeLookupById[id]["j"] == self.jLen -1))):
                    self.connectedToExt = 1
                for neighbor in self.nodeLookupById[id]["neighbor"]:
                    if (neighbor["id"] not in self.visited and neighbor["id"] in self.non_visited):
                        self.stack.append(neighbor["id"])
            if (self.stack == []):
                if (self.connectedToExt):
                    self.connectedToExt = 0
                    self.visited = []
                for id in self.visited:
                    self.toFlip.append(id)
                if (self.non_visited != []):
                    self.visited = []
                    self.stack.append(self.non_visited[0])

    def flipSurroundedRegions(self, board):
        for id in self.toFlip:
            board[self.nodeLookupById[id]["i"]][self.nodeLookupById[id]["j"]] = "X"

    def solve(self, board):
        if (board):
            self.idLookupByIndex = [[-1 for j in board[0]] for i in board]
            self.iLen = len(board)
            self.jLen = len(board[0])
            self.createRegionsGraph(board)
            if (self.non_visited != []):
                self.findSurroundedRegions(0)
            if (self.toFlip != []):
                self.flipSurroundedRegions(board)
