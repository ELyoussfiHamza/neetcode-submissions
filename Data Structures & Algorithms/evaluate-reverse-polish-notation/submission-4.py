class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        st = deque()
        i = 0
        
        while i < n:
            curr = tokens[i]
            if curr in {'+','-','*',"/"}:
                op2 = st.pop()
                op1 = st.pop()
                if curr == '+':
                    st.append(int(op1) + int(op2))
                elif curr == '-':
                    st.append(int(op1) - int(op2))
                elif curr == '*':
                    st.append(int(op1) * int(op2))
                else:
                    st.append(int(op1)/int(op2))
            else:
                st.append(curr)
            i+=1
        
        return int(st[0])