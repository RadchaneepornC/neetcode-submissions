class Solution:
    # My attempt:
    # Time Complexity:  O(nlogn), when n = len(nums)
    # Extra Space Complexity: O(n), when n= len(nums), it uses in the element_n_count, element_reverse

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n ==1 and k==1:
            return nums

        element_n_count = {}
        element_reverse = []
        result = []
        # time complexity: O(n), n = len(nums)
        for i in nums:
            if i in element_n_count:
                element_n_count[i] +=1
            else: 
                element_n_count[i] =1
        
        # time complexity: O(n), n = len(nums)
        for a,b in element_n_count.items():
            element_reverse.append((b,a)) #(count,element) 

        # time complexity: O(nlog(n))
        filter_top_k = sorted(element_reverse)[-k:]

        # time complexity: O(k), k = top k numbers of the element 
        for count,element in filter_top_k:
            result.append(element)

        return result
