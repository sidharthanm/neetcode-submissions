class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edge =set()
        ROWS,COLUMNS = len(board),len(board[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        def flood(r,c):
            
            if ((r,c) in edge ) or not( 0<=r<ROWS and 0<=c<COLUMNS):
                return
            
            if board[r][c] == "X":
                return
            
            board[r][c] ="T"
            edge.add((r,c))

            for i, j in directions:
                flood(r+i,c+j)
            
            return
        

        
        for i in range(ROWS):
            flood(i,0)
            flood(i,COLUMNS-1)
        for i in range(COLUMNS):
            flood(0,i)
            flood(ROWS-1,i)

        # print(edge,visit)
        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column]=="O":
                    board[row][column]="X"
                if board[row][column]=="T":
                    board[row][column]="O"
            

            
