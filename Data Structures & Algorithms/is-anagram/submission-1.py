class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        # store the value and number of occurance in dict_s
        for i in s:
            if i in dict_s:
                dict_s[i]+=1
            else:
                dict_s[i]=1

        # store the value and number of occuranc in dict_t
        for j in t:
            if j in dict_t:
                dict_t[j]+=1
            else:
                dict_t[j]=1
        
        for k in dict_s:
            if (not k in dict_t) or (dict_t[k] != dict_s[k]):
                return False
        
        return True


        

