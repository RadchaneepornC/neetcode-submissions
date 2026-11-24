class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n ==1 and k==1:
            return nums

        element_n_count = {}
        element_reverse = []
        result = []
        for i in nums:
            if i in element_n_count:
                element_n_count[i] +=1
            else: 
                element_n_count[i] =1
        
        # can't do like this, since the reverse will switch the count to the key of dict, but the key of dict should be unique 
        for a,b in element_n_count.items():
            element_reverse.append((b,a)) #(count,element) 


        filter_top_k = sorted(element_reverse)[-k:]

        for count,element in filter_top_k:
            result.append(element)

        return result
