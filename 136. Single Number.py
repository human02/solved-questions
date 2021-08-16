""" 
Level - Easy 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
 """

class Solution:
    def singleNumber_hashTable(self, nums: List[int]) -> int:
        l={}
        for i in nums:
            if i in l:
                l[i]+=1
            else:l[i]=1
            
        print(l)
        for i in l:
            if(l[i]==1):
                return i


class Solution:
    def singleNumber_math(self, nums: List[int]) -> int:
        # The idea is -> 2*(a+b+c)−(a+a+b+b+c)=c
        return 2 * sum(set(nums)) - sum(nums)

class Solution:
    """
    Concept

    If we take XOR of zero and some bit, it will return that bit
    a XOR 0 = a⊕0 = a
    
    If we take XOR of two same bits, it will return 0
    a XOR a = a⊕a = 0
    a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = a⊕b⊕a = (a⊕a)⊕b = 0⊕b = b

    """
    def singleNumber_bitManupilation(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
            