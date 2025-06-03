class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        return self.stack.append(val)
        
        
    def pop(self):
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        mini = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < mini:
                mini = self.stack[i]
        return mini

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
