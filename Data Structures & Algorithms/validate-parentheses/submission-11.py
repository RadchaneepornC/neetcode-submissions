class Solution:
    # my second attempt: based on the NeetBot hints, this version passes all the test cases
    # hint 1: Notice that your current logic tries to divide the problem into two fixed shapes: adjacent pairs like ()[]{} or purely nested palindromes like ([{}]). However, brackets can be arbitrarily nested and sequenced together, such as {[()()]([])}. What kind of data structure can handle this "most recently opened, first to be closed" behavior?
    # hint 2: When encountering a closing bracket, it must match the most recently seen unmatched opening bracket. This Last-In, First-Out (LIFO) order suggests using a stack (which can be represented by a Python list).
# hint 3: Iterate through the string character by character. If the character is an opening bracket ((, [, {), push it onto your stack. If it is a closing bracket, check whether the stack is empty (which means an invalid closing bracket arrived first) or if the top of the stack does not match the current closing bracket. If it matches, pop from the stack.

    # some test cases used during implementation
    # test case 1: s = "{[()()]([])}"
    # test case 2: s = "()[]{}"
    # test case 3: s = "[]", s = "([{}])"

    # time complexity: O(n), n = len(s) -- each character is visited once; append/pop on a list are O(1)
    # extra space complexity: O(n) -- the stack list1 can hold up to n/2 opening brackets (e.g. "(((...)))");
#                         paren_dict (3 fixed entries) and i are O(1)
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 != 0:
            return False
        paren_dict = {'(':')','[':']','{':'}'}
        list1 = []
        for i in s:
            if i in paren_dict: # push the opening bracket onto the stack (list1)
                list1.append(i)
            else:
                if not list1: # a closing bracket arrived with no opening bracket to match
                    return False
                elif paren_dict[list1[-1]]!=i:
                    return False # the top of the stack does not match the current closing bracket
                else: # the top of the stack matches the current closing bracket
                    list1.pop(-1)

        if len(list1)>0: # some unmatched opening brackets remain that were never popped
            return False
        else:
            return True # every bracket was matched and popped


        