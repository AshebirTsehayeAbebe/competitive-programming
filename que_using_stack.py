class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.length = 0

    def push(self, x: int):
        self.stack1.append(x)
        self.length += 1

    def pop(self):
        if self.stack2:
            self.length -= 1
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                self.length -= 1
                return self.stack2.pop()

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                return self.stack2[-1]

    def empty(self):
        return not bool(self.length)
