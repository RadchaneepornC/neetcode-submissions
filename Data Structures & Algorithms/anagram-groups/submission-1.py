class Solution:
    # anagrams = the unique str is same and the number of each str is same
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if not strs or n == 1: # empty list and one element list
            return [strs]
        
        key_with_elm = {}

        for i in strs:
            key = ''.join(sorted(i)) # sort return the list of individual sort str
            if key not in key_with_elm:
                key_with_elm[key]=[i]
            else:
                key_with_elm[key].append(i)

        answer = list(key_with_elm.values())

        return answer

        
        
        
        

            
        
