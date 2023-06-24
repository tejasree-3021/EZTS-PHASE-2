class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def search(root,key):
    if root is None or root.val==key:
        return root.val
    if root.val<key:
        return search(root.right,key)
    return search(root.left,key)
r=Node(100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
inorder(r)
key=int(input("enter the value:"))
a=search(r,key)
if a==key:
    print("found",key)
else:
    print("not found")