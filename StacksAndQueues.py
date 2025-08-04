#Stack Implementation (LIFO)
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __repr__(self):
        return str(self.items)


#Queue Implementation (FIFO)
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __repr__(self):
        return str(self.items)

stack = Stack()
stack.push(5)
stack.push(10)
print("Stack after push:", stack)
stack.pop()
print("Stack after pop:", stack)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("Queue after enqueue:", queue)
queue.dequeue()
print("Queue after dequeue:", queue)
