#creaing node
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_start(self): #delete at start
        temp=self.head
        self.head=temp.next
        temp.next=None
        temp.prev=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        prev.next=None
        temp.prev=None
    

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
n3=node(40)
n3.prev=n2
n2.next=n3
obj.display()
print("")
obj.delete_start()
obj.display()
print("")
obj.delete_end()
obj.display()
