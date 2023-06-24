#creaing node
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insert_end(self):
        n=node(143)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n=prev=temp
    def insert_pos(self,pos):
        n=node(12)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
        
        
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#temp assigned to first node
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("<->",end=" ")
                temp=temp.next

obj=dll()
#node creation-initializing
n=node(10)
obj.head=n
n1=node(20)
n1.prev=n
n.next=n1
n2=node(30)
n2.prev=n1
n1.next=n2
obj.display()
print("Inserting before 300")
obj.display()
print("")
print("After inserting 300")
obj.insert_start()
obj.display()
print("")
obj.insert_end()
obj.display()
print("")
obj.insert_pos(2)
obj.display()
print("")