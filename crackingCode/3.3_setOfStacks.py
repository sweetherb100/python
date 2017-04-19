'''
*Question : Set of Stacks
SetOfStacks should be composed of several stacks, and should create a new stack
once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should 
behave identically to a single stack

*Outline
1) Implement Stack class and Stacks class using Stack class
2) Initialize first stack in the stacklist (careful)
-> self.stacklist.append(Stack())
'''

class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def printStack(self):
        return self.items

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)


class Stacks():
    def __init__(self):
        self.stacklist=[]
        self.max_stack_size=3
        #initialize first stack in the stacklist
        self.stacklist.append(Stack())

    def push(self,item):
        st=self.getLastStack()
        if self.max_stack_size == st.size():
            newSt = Stack()
            newSt.push(item)
            self.stacklist.append(newSt)
        else:
            st.push(item)

    def pop(self):
        st=self.getLastStack()
        if st.is_empty() is False:
            st.pop()
            if st.is_empty(): #to match the count of Stacks
                self.stacklist.pop()
        else :
            print('there is no item in Stacks')

        #If so, getStackCount doesn't match the real count of Stacks (WRONG WAY)
        # if st.is_empty():
        #     self.stacklist.pop()
        #     st = self.getLastStack()
        #     st.pop()
        # else:
        #     st.pop()

    def getLastStack(self):
        return self.stacklist[-1]

    def getStackCount(self):
        return len(self.stacklist)

    def printStacks(self):
        result=[]
        for stack in self.stacklist:
            for item in stack.items:
                result.append(item)
        return result


#use Stacks class, not Stack class
stacks=Stacks()
stacks.push(5)
stacks.push(3)
stacks.push(2)
stacks.push(7)
print(stacks.printStacks()) #[5, 3, 2, 7]
print(stacks.getStackCount()) #2
stacks.pop()
print(stacks.printStacks()) #[5, 3, 2]
print(stacks.getStackCount()) #1
stacks.pop()
print(stacks.printStacks()) #[5, 3]
print(stacks.getStackCount()) #1







