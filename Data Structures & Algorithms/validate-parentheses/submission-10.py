class Solution:
    # test case 1: s="{[()()]([])}"
    # test case 2: s="()[]{}"
    # test case 3: s = "[]", s= "([{}])"
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 != 0:
            return False
        paren_dict = {'(':')','[':']','{':'}'}
        list1 = []
        for i in s:
            if i in paren_dict:
                list1.append(i)
            else:
                if not list1: # closing bracket arrived first
                    return False
                elif paren_dict[list1[-1]]!=i:
                    return False #  the top of the stack does not match the current closing bracket. 
                else: # the top of the stack match the current closing bracket.            
                    list1.pop(-1)
        
        if len(list1)>0: # remain the unmatch that can't be pop out
            return False
        else:
            return True # all things match and be pop out


        