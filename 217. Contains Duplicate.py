class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements={}
        for i in nums:
            if i in elements:
                return True
            else:
                elements[i]=1
        return False
        