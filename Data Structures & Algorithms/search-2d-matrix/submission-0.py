class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find target row
        found_row = False
        rowIndex = 0
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l - (l - r) // 2

            if target < matrix[mid][0]:
                    r = mid - 1
            elif target > matrix[mid][-1]:
                    l = mid + 1
            else: 
                rowIndex = mid
                found_row = True
                break

        if not found_row: return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l - (l - r) // 2
            if matrix[rowIndex][mid] == target:
                return True
            elif matrix[rowIndex][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            