class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = []
        front.append(1)
        temp = 1
        for i in range(0, len(nums)-1):
            temp = temp*nums[i]
            front.append(temp)

        back = []
        back.append(front[len(front)-1])
        temp = 1
        for i in range(len(nums)-1, 0,-1):
            temp = temp*nums[i]
            # back.insert(0, front[i-1]*temp)
            back.append(front[i-1]*temp)
        
        back.reverse()
        return back

        