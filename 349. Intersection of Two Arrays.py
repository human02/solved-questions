"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

# Using Python Set type methods
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        return(list(nums1.intersection(nums2)))

"""
This is a Facebook interview question.
They ask for the intersection, which has a trivial solution using a hash or a set.

Then they ask you to solve it under these constraints:
O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
You are told the lists are sorted.

Cases to take into consideration include:
duplicates, negative values, single value lists, 0's, and empty list arguments.
Other considerations might include
sparse arrays.

function intersections(l1, l2) {
    l1.sort((a, b) => a - b) // assume sorted
    l2.sort((a, b) => a - b) // assume sorted
    const intersections = []
    let l = 0, r = 0;
    while ((l2[l] && l1[r]) !== undefined) {
       const left = l1[r], right = l2[l];
        if (right === left) {
            intersections.push(right)
            while (left === l1[r]) r++;
            while (right === l2[l]) l++;
            continue;
        }
        if (right > left) while (left === l1[r]) r++;
         else while (right === l2[l]) l++;
        
    }
    return intersections;
}
"""