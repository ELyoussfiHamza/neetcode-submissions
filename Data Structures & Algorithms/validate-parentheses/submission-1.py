class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        brackets = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        st = deque()
        for e in s:
            if e in brackets:
                st.append(e)
            else:
                if len(st) == 0:
                    return False
                last = st.pop()
                if e != brackets[last]:
                    return False
        
        return len(st) == 0