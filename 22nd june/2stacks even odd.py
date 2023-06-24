stack=[]
even_stack=[]
odd_stack=[]
def push():
    element=int(input())
    if element%2==0:
        even_stack.append(element)
    else:
        odd_stack.append(element)
  
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
def display():
        l=int(input())
        if l==1:
            print(even_stack)
        else:
            print(odd_stack)
            
        
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

