
def n_faktorial(n):
    if n==1:
        return 1
    else:
        return n*n_faktorial(n-1)

#print(n_faktorial(5))

class Stock:
    def __init__(self):
        self.stack=[]
        
    def isEmpty(self):
        return len(self.stack)==0

    def push(self,n):
        self.stack.append(n)
        return True
    def pop(self,):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return  self.stack.pop()
    def peek(self):
        if isEmpty():
            return "Stack is Empty"
        return  self.stack[-1]
    def __repr__(self):
        return f"Stack({self.stack})"

stack=Stock()
print(stack.isEmpty())
stack.push(7)
stack.push(5)
stack.push(7)
print(stack.isEmpty())
print(stack)
stack.pop()
stack.pop()
stack.pop()
print(stack.isEmpty())
            
        
