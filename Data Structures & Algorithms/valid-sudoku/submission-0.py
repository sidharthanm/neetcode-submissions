class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = dict()
        COLUMNS = dict()
        BOX = dict()
        for column in range(0,9):
            for row in range(0,9):
                if board[column][row] == '.':
                    continue
                
                value = board[column][row] 
                if row in ROWS:
                    if value in ROWS[row]:
                        return False
                    else:
                        ROWS[row].append(value)
                else:
                    ROWS[row] = [value,]

                if column in COLUMNS:
                    if value in COLUMNS[column]:
                        return False
                    else:
                        COLUMNS[column].append(value)
                else:
                    COLUMNS[column] = [value,]
                
                if (row//3,column//3) in BOX:
                    if value in BOX[(row//3,column//3) ]:
                        return False
                    else:
                        BOX[(row//3,column//3) ].append(value)
                
                else:
                     BOX[(row//3,column//3) ] = [value,]
        return True


            

