#  Medium Level
# most efficient, time complexity: O(n)
class Solution:
    # time complexity: O(n)
    # extra space complexity: O(1), left, right
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The key idea: left part × right part
      
        # [1, 2, 3, 4] --> []
        # i = 0 : left = left; right = nums[i+1] * right(i=1) = 24; result = 24
        # i = 1 : left =left (i=0) * nums[i-1] = 1*1 = 1; right = nums[i+1] * right(i=2)= 3*4 = 12; result = 12
        # i = 2 : left = left (i=1)* nums[i-1] = 1*2 = 2; right = nums[i+1]*right (i=3) = 1*4 = 4; result = 8
        # i = 3 : left = left (i=2) * nums[i-1]= 2*3 = 6; right = right; result = 6
        
    
        n = len(nums)
        result = [1]*n

        # multiply the left for every index
        left = 1
        for i in range(n):
            result[i] = left
            left*=nums[i]

        # multiply the right for every index having the left element already
        right = 1
        for j in range(n-1, -1, -1):
            result[j]*=right
            right*=nums[j]

        return result
# ===============================================================================================================
# more efficient
# class Solution:
#     # time complexity: O(n^2), For each i, the two while loops run i steps plus n−i−1 steps, whichis n−1 steps total
#     # extra space complexity: O(1), i, j,k, (not counting the output list). This is a real improvement over the brute force, which used O(n²) space
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # The key idea: left part × right part
#         # For each index i, the answer is:(product of everything LEFT of  i) × (product of everything RIGHT of i)
#         # [0, 1, 2, 3] --> [6, 0, 0, 0]
#         n = len(nums)
#         result = []
#         for i in range(n):
#             left = 1
#             right = 1
#             k = 0
#             j = i+1
#             while k < i:
#                 left *= nums[k]
#                 k+=1
#             while j < n:
#                 right *= nums[j]
#                 j+=1
#             product = left*right
#             result.append(product)
#         return result

# ===============================================================================================================
# brute force
# class Solution:
    # time complexity: O(n^2), lower loop
    # extra space: O(n^2), dict_k stores n lists, each with n−1 elements, so about n² numbers are held in memory at once
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     dict_k = {}
    #     result = []
    #     for i in range(n):
    #         if i == 0:
    #             dict_k[i] = nums[1:]
    #         elif i == n-1:
    #             dict_k[i] = nums[:n-1]
    #         else:
    #             dict_k[i] = nums[:i]+nums[i+1:]

    #     for j in dict_k.values():
    #         result_mul = 1
    #         for k in j:
    #             result_mul*=k
    #         result.append(result_mul)

    #     return result
# ==============================================================================================================