class QueueUnderflow(ValueError):
    pass
    

class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0
        
    def is_empty(self):
        return self._num == 0
        
    def peek(self):
        if self.is_empty():
            raise QueueUnderflow("in peek")
        return self._elems[self._head]
        
    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1
        
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow("in dequeue")        
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e
        
    def __extend(self):
        old_len = self._len
        self._len = old_len* 2
        new_list = [0] * self._len 
        for i in range(old_len):
            new_list[i] = self._elems[(self._head + i) % old_len]
        self._elems = new_list
        self._head = 0
        
    def __repr__(self):
        return str(self._elems)
        
if __name__ == "__main__":
    q = SQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q)
    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    print(q)
