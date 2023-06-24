# inserting the node at beginning and deleting the first node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.head is None:
            self.head=Node(data)
            self.last=self.data
        else:
            self.last.next=Node(data)
            self.last=self.last.next
            
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
        
            
a_queue=queue()
while True:
    print(' enqueue <value>')
    print('dequeue')
    print('quit')
    do=input("m kavali ra??:").split()
    print("do",do)
    print("do[0]",do[0])
    operation = do[0].strip().lower()
    if operation =='push':
        obj_queue.enqueue()(int(do[1]))
    elif operation == 'pop':
        popped=obj_queue.dequeue()
        if popped is  None:
            print("queue is empty")
        else:
            print("Popped value:",int(popped))
    elif operation == 'quit':
        break
