"""

"""

from collections import deque


class Solution:
    def findNeg(self, arr, k):
        n = len(arr)-1
        i, j = 0, 0
        res = []
        negs = []
        while(j < n):
            if(arr[j] < 0):  # storing negative numbers only
                negs.append(arr[j])
            if(j-i+1 < k):  # increasing window to size = k
                j += 1
            elif(j-i+1 == k):
                # calculating the answer
                if(len(negs) == 0):
                    res.append(0)
                else:
                    res.append(negs[0])
                # Sliding the window now by removing the i related calculation
                    if(arr[i]==negs[0]):
                        negs=negs[1:]
                i += 1
                j += 1
        return res


a = Solution()
arr = [2, -5, -1, -8, 2, 9, 1]
print(f"\n(-)ve in each window = {a.findNeg(arr, 3)}\n")
