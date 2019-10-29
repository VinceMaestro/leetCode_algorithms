class Solution:
    def solve(self, board):
        if (board):
            queue = []
            CONNECTED = "C"
            iLen = len(board)
            jLen = len(board[0])
            for i in range(0, iLen):
                for j in range(0, jLen):
                    if ((i == 0 or i == iLen - 1 or j == 0 or j == jLen - 1) and board[i][j] == "O"):
                        queue.append((i,j))

            while (queue):
                i, j = queue.pop()
                board[i][j] = CONNECTED
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (i + x >= 0 and i + x < iLen and j + y >= 0 and j + y < jLen and board[i + x][j + y] == "O"):
                        queue.append((i + x, j + y))

            NOT_CONNECTED = "O"
            for i in range(0, iLen):
                for j in range(0, jLen):
                    if (board[i][j] == NOT_CONNECTED):
                        board[i][j] = "X"
                    elif (board[i][j] == CONNECTED):
                        board[i][j] = "O"
