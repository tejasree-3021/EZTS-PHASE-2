stack=[]
def push():
    element=int(input())
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
def display():
    if not stack:
        print("stack is empty")
    else:
        print("1 or 2")
        l=int(input())
        if l==1:
            print("even")
            for i in stack:
                if i%2==0:
                  print(i)
        else:
            print("odd")       
            for i in stack:
                if i%2!=0:
                    print(i)
def top():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print(" peak element:",e)
      
while True:
    print("select operation 1.push 2.pop 3.display 4.top")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        top()
        
    else:
        break

