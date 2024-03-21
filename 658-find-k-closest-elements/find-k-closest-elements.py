class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find x or closest to x
        # two pointers, span them
        # we have two sorted arrays, combine them
        left = 0
        right = len(arr) - 1
        mid = 0
        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                break
            
            if mid == left:
                break
            
            if arr[mid] < x:
                left = mid
            elif arr[mid] > x:
                right = mid
        
        if arr[mid] == x:
            left = mid - 1
            right = mid + 1
        else:
            mid = left if (x - arr[left] <= arr[right] - x) else right
            left = mid - 1
            right = mid + 1
        
        while (left >= 0) and (right < len(arr)) and (right - left - 1 < k):
            if x - arr[left] <= arr[right] - x:
                left = left - 1
            else:
                right = right + 1
        
        while left >= 0 and right - left - 1 < k:
            left = left - 1
        
        while right < len(arr) and right - left - 1 < k:
            right = right + 1
        
        return arr[left + 1 : right]


                


