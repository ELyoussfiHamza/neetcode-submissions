class MinStack:

    def __init__(self):
        self.st = deque()
        self._min = float('inf')
    def push(self, val: int) -> None:
        self._min = min(self._min , val)
        self.st.append((val , self._min))
        
    def pop(self) -> None:
        self.st.pop()
        if len(self.st) > 0:
            self._min = self.st[-1][1]
        else:
            self._min=float('inf')


    def top(self) -> int:
        
        return self.st[-1][0]

    def getMin(self) -> int:
        return self._min
