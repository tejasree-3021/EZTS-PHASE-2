class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is  None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end="")
                else:
                    print(temp.data,end="")
                temp=temp.next
obj=sll()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()
print("")
obj.insert_position(0,1000)
obj.display()



