class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None  #nref = next node reference
        self.pref = None  #pref = prev node reference
        
class doublyLL:
    def __init__(self):
        self.head = None
        
    def printLL(self):
        if self.head is None:
            print('Empty LinkedList')
        else:
            n=self.head
            while n is not None:
                print(n.data,end = "->")
                n=n.nref
            print('\n')
            
    def printLL_rev(self):
        if self.head is None:
            print('Empty LinkedList')
        else:
            n=self.head
            while n.nref is not None:
                
                n=n.nref
            while n is not None:
                
                print(n.data,end = "->")
                n = n.pref
                print('\n')
                
    def ins_empty(self,data):  #inserting in empty LinkedList
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('LinkedList is not empty')
        
    def add_begin(self,data):
        if self.head is None:
            ins_empty(data)
            
        else:
            n = self.head
            new_node = Node(data)
            new_node.nref = self.head 
            self.head = new_node
            
    
            
            
            
    
DLL = doublyLL()    
DLL.ins_empty(20)
DLL.add_begin(10)
DLL.add_end(30)
DLL.printLL()
        
        
    
