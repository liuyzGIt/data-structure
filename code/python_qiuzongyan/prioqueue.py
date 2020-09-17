class ProiQueueError(ValueError):
    pass
    
class ProiQueue: # 小顶堆
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if self._elems:
            self._buildheap()
        
    def is_empty(self):
        return not self._elems
        
    def enqueue(self, e):
        self._elems.append(e)
        self._shiftup(e, len(self._elems)-1, 0)
        
    def dequeue(self):
        if self.is_empty():
            raise ProiQueueError("in dequeue")
        e0 = self._elems[0]
        e = self._elems.pop()
        if len(self._elems) > 0:
            self._shiftdown(e, 0, len(self._elems))
        return e0
        
    def peek(self):
        if self.is_empty():
            raise ProiQueueError("in peek")
        return self._elems[0]
    
    def _buildheap(self):
        end = len(self._elems)
        for i in range(len(self._elems) // 2, -1, -1):
            self._shiftdown(self._elems[i], i, end)
    
    def _shiftup(self, e, begin, end):
        elems, i, j = self._elems, begin, (begin - 1) // 2        
        while i > 0:
            if j > 0 and elems[j] > elems[j+1]:
                j +=1
            if e < elems[j+1]:
                break
            elems[i] = elems[j]
            i, j = j, (j-1) // 2            
        elems[i] = e
            
    
    def _shiftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:                        
            if j+1 < end and elems[j] > elems[j+1]:
                j+=1            
            if elems[j] > e:
                break
            elems[i] = elems[j]
            i, j = j, j*2+1
            
        elems[i] = e
    
if __name__ == "__main__":
    q = ProiQueue([3,2,1])
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    
