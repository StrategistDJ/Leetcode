class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        return
            

    def pop(self) -> int:
        value = self.queue[0]
        self.queue.remove(value)
        return value

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()