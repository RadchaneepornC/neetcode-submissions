class Solution:
    
    # second attempt with the hints from NeetBot
    # hint 1: Notice that you are converting each string to a set with set(i), which loses character frequencies (e.g., 'a' and 'aa' become the same set). Is there a way to represent the characters in a word that preserves both the characters and their exact counts?
    # hint 2: If two strings are anagrams, sorting their characters directly (without set()) will result in identical sequences. For example, 'stop' and 'pots' both become ['o', 'p', 's', 't'] when sorted.
    # hint 3: Initialize a hash map (defaultdict(list) or standard dict). For each word in strs, sort its characters and join them back into a string: key = "".join(sorted(word)). Append the original word to dict[key]. Finally, return list(dict.values()).
    # anagrams = strings with the same unique characters and the same count of each character

    # time complexity: O(n * k log k), n = len(strs), k = length of the longest string
    #                  -- each of the n strings is sorted, and sorting a string of length k costs O(k log k)
    # extra space: O(n * k) -- key_with_elm stores every string once in its lists, plus up to n keys of length up to k
    #              (worst case: every string is its own unique anagram group)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if not strs or n == 1: # empty list or one-element list
            return [strs]

        key_with_elm = {}

        for i in strs:
            key = ''.join(sorted(i)) # sorted() returns a list of the string's characters in sorted order; join turns it back into a string
            if key not in key_with_elm:
                key_with_elm[key]=[i]
            else:
                key_with_elm[key].append(i)

        answer = list(key_with_elm.values())

        return answer
            
        
        
        

            
        
