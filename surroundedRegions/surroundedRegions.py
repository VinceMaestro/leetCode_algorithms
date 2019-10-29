# entourer la map de z
# Verifier si chaque o est relie a un z
# hashMap visited
# on parcourt tout sans s'arreter si on trouve un Z
# quand tout a ete parcourut, si on a trouve un z, tout les O visites sont pop de total
# quand on ne trouve pas de z, il sont pop de total et append dans non_connectes
# quand la liste des O a investiguer est vide on transforme tout les O dans non_connectes en X

# def solve(self, board: List[List[str]]) -> None:

class Solution:
    def __init__(self):
        self.visited = []
        self.nodeLookupById = {}
        self.non_visited = []
        self.connectedToExt = 0
        self.toFlip = []

    def newNode(self, id, i, j):
        node = {"id": id, "i": i, "j": j, "neighbor": []}
        self.nodeLookupById[id] = node
        self.idLookupByIndex[i][j] = id
        self.non_visited.append(id)
        return (node)

    def mapRegions(self):
        return ()

    def lookForAdjacentAndConnect(self, id, i, j):
        neighborId = -1
        if (i > 0):
            neighborId = self.idLookupByIndex[i - 1][j]
            if (neighborId > -1):
                # print("Add upper neighbor from i = {}, j = {}".format(i, j))
                self.nodeLookupById[id]["neighbor"].append(self.nodeLookupById[neighborId])
                self.nodeLookupById[neighborId]["neighbor"].append(self.nodeLookupById[id])
                if (id == 11 or id == 15 or id == 16):
                    print("id = {} , link up".format(id))
                    print(self.nodeLookupById[id])
        if (j > 0):
            neighborId = self.idLookupByIndex[i][j - 1]
            if (neighborId > -1):
                # print("Add left neighbor from i = {}, j = {}".format(i, j))
                self.nodeLookupById[id]["neighbor"].append(self.nodeLookupById[neighborId])
                self.nodeLookupById[neighborId]["neighbor"].append(self.nodeLookupById[id])
                if (id == 11 or id == 15 or id == 16):
                    print("id = {} , link left".format(id))
                    print(self.nodeLookupById[id])

    def createRegionsGraph(self, board):
        id = 0
        for i in range(0, self.iLen):
            for j in range(0, self.jLen):
                if (board[i][j] == "O"):
                    node = self.newNode(id, i, j)
                    self.lookForAdjacentAndConnect(id, i, j)
                    id += 1
        self.maxId = id - 1
        # Verif bonne creation du Graph et bonnes connexions

    def printGraph(self):
        for id in range(0, self.maxId + 1):
            print(self.nodeLookupById[id])

    def findSurroundedRegions(self, id):
        # for node in nodeLookupById:
        self.visited.append(id)
        print("Visited : {}".format(self.visited))
        self.non_visited.remove(id)
        print("Non Visited : {}".format(self.non_visited))
        if ((self.nodeLookupById[id]["i"] == 0) or (self.nodeLookupById[id]["i"] == self.iLen - 1) or (self.nodeLookupById[id]["j"] == 0) or (self.nodeLookupById[id]["j"] == self.jLen -1)):
            self.connectedToExt = 1
        for neighbor in self.nodeLookupById[id]["neighbor"]:
            if (neighbor["id"] not in self.visited and neighbor["id"] in self.non_visited): ##Change cette condition pour qu'il arrete de boucler
                self.findSurroundedRegions(neighbor["id"])
        if (self.connectedToExt):
            # print("Deconnect")
            self.connectedToExt = 0
            self.visited = []
        else:
            for id in self.visited:
                self.toFlip.append(id)
        if (self.non_visited != []):
            self.visited = []
            # print("IF - Non Visited : {}".format(self.non_visited))
            self.findSurroundedRegions(self.non_visited[0])

    def flipSurroundedRegions(self, board):
        for id in self.toFlip:
            board[self.nodeLookupById[id]["i"]][self.nodeLookupById[id]["j"]] = "X"

    def solve(self, board):
        if (board):
            self.idLookupByIndex = [[-1 for j in board[0]] for i in board]
            # stack = z
            self.iLen = len(board)
            self.jLen = len(board[0])

            self.createRegionsGraph(board)
            # self.printGraph()

            if (self.non_visited != []):
                self.findSurroundedRegions(0)
            print("To Flip {}".format(self.toFlip))
            if (self.toFlip != []):
                self.flipSurroundedRegions(board)

            # print(newBoard)
