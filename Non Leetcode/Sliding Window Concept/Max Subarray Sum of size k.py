"""
Maximum Subarray Sum of size 'k'

Note: Subarray is continiuos
"""


class Solution:
    def findMax(self, nums, k):
        i = 0  # denotes the start
        j = 0  # denotes the end
        mx = -1
        tot = 0
        # Sliding window - fixed
        while(j < len(nums)-1):
            tot = tot + nums[j]  # adding at every steps
            if(j-i+1 < k):  # creating the window to appropriate size
                j += 1
            elif(j-i+1 == k):  # when window is of appropriate size
                # finding max of sum until now and mx and storing it in mx.
                mx = max(mx, tot)
                tot -= nums[i]  # removing the sum of start slided element
                i += 1  # moving window to right
                j += 1  # moving window to right
        return mx


a = Solution()
arr = [2, 5, 1, 8, 2, 9, 1]
print(f"\nMaximum Subarray Sum = {a.findMax(arr, 3)}\n")
