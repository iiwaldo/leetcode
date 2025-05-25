def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_dict = [{} for _ in range(9)]
        column_dict = [{} for _ in range(9)]
        box_dict = [{} for _ in range(9)]
        for row in range(9):
            for col in range(9):
                box_index = (row // 3) * 3 + (col // 3)
                value = board[row][col]
                if value == ".":
                    continue
                if value in row_dict[row] or value in column_dict[col] or value in box_dict[box_index]:
                     return False
                row_dict[row][value] = 1
                column_dict[col][value] = 1
                box_dict[box_index][value] = 1
        return True
        
            
                

        




isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
