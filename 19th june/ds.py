l=[]
n=int(input())
for i in range(0,n):
    ele=(int(input("enter elements")))
    l.append(ele)
print(l)
ch=int(input("enter operation choose \n1.insert 2.delete 3.search 4.sort 5.display\n"))
if ch==1:
    n1=int(input())
    print("enter element")
    for i in range(0,n1):
        num=int(input())
        l.append(num)
    print(l)
elif ch==2:
    n1=int(input())
    print("enter element")
    for i in range(0,n1):
        num1=int(input())
        l.remove(num1)
        print(l)
elif ch==3:
    a=int(input())
    if a in l:
        print("found")
    else:
        print("notfound")
elif ch==4:
    l.sort()
    print("sorted elements")
    print(l)
elif ch==5:
    print(l)
    
   
    
          
       


