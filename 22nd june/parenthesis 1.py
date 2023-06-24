open_list=["(","[","{"]
closed_list=[")","]","}"]
def check(str):
    stack=[]
    for i in str:
        if i in open_list:
            stack.append(i)
        elif i in closed_list:
            pos=closed_list.index(i)
            if (len(stack)>0) and (open_list[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "unbalenced"
                

    if len(stack)==0:
        return "Balence"
    else:
        return "unbalence"
string=input()
print(check(string))
  
             