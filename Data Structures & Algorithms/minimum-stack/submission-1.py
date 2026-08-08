class MinStack:

    def __init__(self):
        self.s = list()
        self.c = None
    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(0)
            self.c = val
        else:

            tmp = val -self.c
            self.s.append(tmp)
            if tmp <0:
                self.c = val

    def pop(self) -> None:
        tmp = self.s.pop()
        if tmp <0:
            self.c = self.c - tmp

                

    def top(self) -> int:
        if self.s[-1]<0:
           return self.c 
        return self.s[-1]+self.c

    def getMin(self) -> int:
        return self.c
