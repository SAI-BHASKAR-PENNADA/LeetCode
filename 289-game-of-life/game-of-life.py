class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0,1], [1,0], [-1,0], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
        def neighbours(row, col):
            ans = 0
            for direction in directions:
                newRow = row+direction[0]
                newCol = col+direction[1]
                if newRow < len(board) and newCol < len(board[0]) and newRow >= 0 and newCol >= 0 and board[newRow][newCol] == 1:
                    ans += 1
                    if ans > 3:
                        break
            # print(row, col, ans)
            return ans
        
        updates = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                count = neighbours(row, col)
                if board[row][col] == 1:
                    if count < 2 or count > 3:
                        updates.append([row,col])
                else:
                    if count == 3:
                        updates.append([row,col])
        # print(updates)
        for update in updates:
            if board[update[0]][update[1]] == 1:
                board[update[0]][update[1]] = 0
            else:
                board[update[0]][update[1]] = 1
