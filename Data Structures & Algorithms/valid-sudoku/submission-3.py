class Solution:
    def _checkColumn(self , board: List[List[str]] , c : int) -> bool:
        seen = set()
        for r in range(len(board)):

            if board[r][c] == ".":
                continue
            if (board[r][c].isdigit() is False or board[r][c] == '0' or board[r][c] in seen):
                return False
            seen.add(board[r][c])
        return True
    
    def _checkRow(self , board : List[List[str]] , r : int) -> bool:
        seen = set()
        for c in range(len(board[r])):
            if board[r][c] ==".":
                continue
            if (board[r][c].isdigit() is False or board[r][c] == '0' or board[r][c] in seen):
                return False
            seen.add(board[r][c])
        return True
    
    def _checkBox(self , board : List[List[str]] , r:int , c:int):
        seen = set()
        for i in range(r , r + 3):
            for j in range(c , c + 3):
                
                if board[i][j] ==".":
                    continue

                if (board[i][j].isdigit() is False or board[i][j] == '0'or board[i][j] in seen):
                    return False
                seen.add(board[i][j])
        
        return  True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOXES = [(0 , 0) , (0 , 3) , (0, 6) , (3, 0) , (3 , 3) , ( 3, 6) , (6 , 0), (6,3), (6 , 6)]

        for i in range(len(board)):
            if self._checkRow(board , i) is False:
                return False

        for j in range(len(board[0])):
            if self._checkColumn(board , j) is False:
                return False

        for (r , c) in BOXES:
            if self._checkBox(board , r , c) is False:
                return False

        return True

