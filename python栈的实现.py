class Stack: 
    """模拟栈""" 
    def __init__(self): 
        self.items = [] 

    def isEmpty(self): 
        return len(self.items)==0  

    def push(self, item):
       
        self.items.append(item) 

    def pop(self): 
        return self.items.pop()  

    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 

    def size(self): 
        return len(self.items)

s=Stack() 
print(s.isEmpty()) 
s.push(4) 
s.push('dog') 
print(s.peek()) 
s.push(True) 
print(s.size()) 
print(s.isEmpty()) 
s.push(8.4) 
print(s.pop()) 
print(s.pop()) 
print(s.size()) 



###########################################################################
队列
class queue():  
    def __init__(self):  
        self.queue = []  
    def empty(self):  
        return self.queue == []  
    def enqueue(self,data):  
        self.queue.append(data)  
    def dequeue(self):  
        if self.empty():  
            return None  
        else:  
            return self.queue.pop(0)  
    def head(self):  
        if self.empty():  
            return None  
        else:  
            return self.queue[0]  
    def length(self):  
        return len(self.queue)  

if __name__ == '__main__':
    a=queue()
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(5)
    print a.length()
    print a.dequeue()
    print a.dequeue()
    print a.dequeue()
    
