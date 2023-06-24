#creaing node
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
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