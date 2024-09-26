class Solution:
    def recursion(self, visited, board, curIndex, curRow, curCol, word):
        if curIndex == len(word):
            return True
        if curRow < 0 or curRow >= len(board) or curCol < 0 or curCol >= len(board[0]) or visited[curRow][curCol]:
            return False
        
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if board[curRow][curCol] == word[curIndex]:
            # print("found - ", word[curIndex], " at ", curRow, " ", curCol)
            visited[curRow][curCol] = True
            for move in moves:
                if self.recursion(visited, board, curIndex+1, curRow+move[0], curCol+move[1], word):
                    return True
            visited[curRow][curCol] = False
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        given = {}
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] in given:
                    given[board[row][col]] += 1
                else:
                    given[board[row][col]] = 1
        
        for ch in word:
            if ch in given:
                given[ch] -= 1
                if given[ch] == 0:
                    del given[ch]
            else:
                return False
        
        # if len(given) != 0:
        #     return False

        # print("going for recursion")

        visited = []
        for i in range(0, len(board)):
            helper = [False]*len(board[0])
            visited.append(helper)

        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == word[0]:
                    if self.recursion(visited, board, 0, row, col, word):
                        return True
        return False


        

            
