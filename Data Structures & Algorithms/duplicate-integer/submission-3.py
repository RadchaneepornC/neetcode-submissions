class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        result = {}
        dup = False
        for i in nums:
            if i in result:
                dup = True
                result[i]+=1
            else:
                result[i]=1
        return dup

        