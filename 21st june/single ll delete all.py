class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None

    def delete_start(self): #delete at start
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def delete_end(self):  #delete at end
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end="")
                #temp.data means first nodes data
                temp=temp.next # establishing linked list
obj=singlelinkedlist()
# node creation - initialising
n=Node(10)# so n.data in node class will be 10
obj.head=n    #assigning first node as head
n1=Node(20)
obj.head.next=n1   # next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print(" at position ")
obj.delete_position(2)
obj.display()
print(" ")
print(" at start ")
obj.delete_start()
obj.display()
print(" ")
print(" at end ")
obj.delete_end()
obj.display()