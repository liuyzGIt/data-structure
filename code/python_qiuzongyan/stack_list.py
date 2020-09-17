class StackUnderflow(ValueError):
    pass
    
    
class SStack:
    def __init__(self):
        self._elems = []
        
    def is_empty(self):
        return not self._elems
    
    def push(self, e):
        self._elems.append(e)
    
    def pop(self):
        if self.is_empty():
            raise StackUnderflow("in pop")
        return self._elems.pop()
        
    def top(self):
        if self.is_empty():
            raise StackUnderflow("in pop")
        return self._elems[-1]
        
        
if __name__ == "__main__":
    s = SStack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    print(s.pop())        
    print(s.top())        
    print(s.pop())        
    print(s.pop())        
    print(s.pop())        
