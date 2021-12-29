class Node:
    def __init__(self,data):
        self.data=data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def printLL(self):
        if self.head is None:
            print('Empty LinkedList')
        else:
            n=self.head
            while n is not None:
                print(n.data,end = "->")
                n=n.ref
            print('\n')    
    def add_begin(self,data):
        new_node = Node(data)  #node creating
        new_node.ref = self.head  # assigning the reference node 
        self.head = new_node 
        
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:  #if empty LinkedList
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:  #traverse till the end of LL
                n = n.ref
            n.ref = new_node    
            
    def add_after(self,data,x): #after a given data
        n = self.head
        while n is not None:
            if x == n.data:
                break
            else:
                n = n.ref
        if n is None:
            print('No element in the LinkedList')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def add_before(self,data,x):    #add before the given data
        
        if self.head is None:
            print('Empty LinkedList')
            return
        
        if self.head.data == x:
            new_node = Node(data) 
            new_node.ref = self.head   
            self.head = new_node 
            return
        
        
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            else:
                n = n.ref
        
        if n.ref is None:
            print('No element in the LinkedList')
            
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    def del_begin(self):
        if self.head is None:
            print('Empty LinkedList')
        
        else:
            self.head = self.head.ref
            
    def del_end(self):
        
        if self.head is None:
            print('Empty LinkedList')
            
        else:    
            n=self.head
            while n.ref.ref is not None:
                n = n.ref  
                
            n.ref = None
            
    def del_by_value(self,x):
        if self.head is None:
            print('LinkedList is Empty')
            return
        
        elif self.head.data == x:
            self.head = self.head.ref
            return
            
        elif self.head.ref.data == x:
            self.head.ref = None
        
        else:
            n = self.head
            
            while n.ref is not None:
                if n.ref.data == x:
                    n.ref = n.ref.ref
                    return
                n = n.ref        
            
            
            
               
                
            
        
            

LL = LinkedList()
LL.add_begin(20)
LL.add_begin(10)
LL.add_end(30)
LL.add_after(50,30)
LL.add_before(40,50)
LL.printLL()
LL.del_begin()
LL.printLL()
LL.del_end()
LL.printLL()
LL.del_by_value(40)
LL.printLL()
