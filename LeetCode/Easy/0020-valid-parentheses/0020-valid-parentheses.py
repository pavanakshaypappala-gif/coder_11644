class Solution(object):
    def isValid(self, s):
        par = {'(': ')', '{': '}', '[': ']'}
        st = []
        for idx in s:
            if idx in par:
                st.append(idx)
            elif not st or par[st.pop()] != idx: 
                return False
        return len(st) == 0
