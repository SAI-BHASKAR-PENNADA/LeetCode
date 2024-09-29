class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first binary search 
        low = 0
        high = len(matrix) - 1

        while low < high:
            if low == high - 1:
                break
            mid = low + (high - low) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                low = mid
            else:
                high = mid - 1
        
        # if low == high:
        #     if matrix[low][0] == target:
        #         return True

        if low == high - 1:
            if matrix[high][0] == target:
                return True
        
        row = low if target < matrix[high][0] else high
        low = 0
        high = len(matrix[row]) - 1
    
        while low < high:
            mid = low + (high - low) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if low == high:
            return matrix[row][low] == target 

