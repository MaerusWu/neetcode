class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_r = collections.defaultdict(set)
        dict_c = collections.defaultdict(set)   
        dict_sq = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dict_r[i]:
                    return False
                dict_r[i].add(board[i][j])

                if board[i][j] in dict_c[j]:
                    return False
                dict_c[j].add(board[i][j])

                squareIndex = (i//3 * 3) + j//3
                if board[i][j] in dict_sq[squareIndex]:
                    return False
                dict_sq[squareIndex].add(board[i][j])

        return True