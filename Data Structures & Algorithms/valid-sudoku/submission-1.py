class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_r = defaultdict(set)
        dict_c = defaultdict(set)
        dict_sq = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dict_r[i]:
                    return False
                if board[i][j] in dict_c[j]:
                    return False
                if board[i][j] in dict_sq[i // 3 * 3 + j // 3]:
                    return False
                
                dict_r[i].add(board[i][j])
                dict_c[j].add(board[i][j])
                dict_sq[i // 3 * 3 + j // 3].add(board[i][j])
        return True