class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        for (int i = 0; i < n; i++) {
            if (!checkRow(i, board) || !checkCol(i, board)) {
                return false;
            }
        }
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                if (!checkBox(i, j, board)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean checkRow(int row, char[][] board) {
        boolean[] seen = new boolean[9];
        for (char c : board[row]) {
            if (c == '.') continue;
            int val = c - '1';
            if (val < 0 || val >= 9 || seen[val]) return false;
            seen[val] = true;
        }
        return true;
    }

    private boolean checkCol(int col, char[][] board) {
        boolean[] seen = new boolean[9];
        for (int i = 0; i < 9; i++) {
            char c = board[i][col];
            if (c == '.') continue;
            int val = c - '1';
            if (val < 0 || val >= 9 || seen[val]) return false;
            seen[val] = true;
        }
        return true;
    }

    private boolean checkBox(int startRow, int startCol, char[][] board) {
        boolean[] seen = new boolean[9];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                char c = board[i + startRow][j + startCol];
                if (c == '.') continue;
                int val = c - '1';
                if (val < 0 || val >= 9 || seen[val]) return false;
                seen[val] = true;
            }
        }
        return true;
    }
}