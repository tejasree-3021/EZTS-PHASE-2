queue=[]
def enqueue():
    element=input()
    queue.append(element)
    print(element)
def dequeue():
    if not  queue:
        print(empty)
    else:
        e=queue.pop(0)
        print(e)
def display():
    print(queue)
while True:
    print("select the option 1.enqueue 2.dequeue 3.display")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    else:
        display()
        