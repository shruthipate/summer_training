class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root
    def sumofele(self,root):
        if root is None:
            return 0
        return root.data+self.sumofele(root.left)+self.sumofele(root.right)
    
    def sumofleft(self,root):
        if root is None:
            return 0
        return root.data+self.sumofele(root.left)+self.sumofele(root.right)
    
    def sumofright(self,root):
        if root is None:
            return 0
        return root.data+self.sumofele(root.left)+self.sumofele(root.right)
    
    def sumofeven(self,root):
        if root is None:
            return 0
        even_sum=0
        if root.data%2==0:
            even_sum=root.data
        return even_sum+self.sumofeven(root.left)+self.sumofeven(root.right)
    
    def evenodd(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return self.evenodd(root.left)+self.evenodd(root.right)+root.data
        else:
            return self.evenodd(root.left)+self.evenodd(root.right)-root.data
        
    def heightt(self,root):
        if(root==None):
            return -1
        return max(self.heightt(root.right),self.heightt(root.left))+1
    
    def bal(self,root):
        return  abs(self.heightt(root.left)-self.heightt(root.right))<=1
    
    def leafnode(self,root):
        if root is None:
            return 0
        if(root.right==None and root.right==None):
            return 1
        return self.leafnode(root.left)+self.leafnode(root.right)
    def leafnodesum(self,root):
        s=0
        if root is None:
            return 0
        if(root.right==None and root.right==None):
            return root.data
        return self.leafnodesum(root.left)+self.leafnodesum(root.right)
    
    def search(self,root,x):
        if root==None: 
            return 0
        if root.data==x:
            return 1
        elif root.data<x:
            return self.search(root.right,x)
        else:
            return self.search(root.left,x)
        
    def depth(self,root,x):
        if root.data==None:
            return -1
        if root.data==x:
            return 0
        elif root.data<x:
            return 1+self.depth(root.right,x)
        else:
            return 1+self.depth(root.left,x)
    def leftview(self,root,c,l):
        if(root==None):
            return 
        if c not in l:
            l.append(c)
            print(root.data)
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)																																																																																																																		
        
    def rightview(self,root,c,l):
        if(root==None):
            return 
        if c not in l:
            l.append(c)
            print(root.data)
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l)
        
    def top_view(self,root,c,d):
        if root==None:
            return
        if c not in d:
            d[c]=root.data
        if c<0 and c in d:
            if root.data>d[c]:
                d[c]=root.data
        self.top_view(root.left,c+1,d)
        self.top_view(root.right,c-1,d)
        return d
        
        
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    '''def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.inorder(root.left)
            self.inorder(root.right)
    def postorder(self,root):
        
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end=" ")'''



t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 2)
t1.create(t1.root, 1)
t1.create(t1.root, 7)
t1.create(t1.root, 20)
t1.create(t1.root, 4)
t1.inorder(t1.root)
print()
'''t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print()'''
print(t1.sumofele(t1.root))
print(t1.sumofeven(t1.root))
print(t1.sumofleft(t1.root.left))
print(t1.sumofright(t1.root.right))
print((t1.sumofright(t1.root.right))-(t1.sumofleft(t1.root.left)))
print(t1.evenodd(t1.root))
print(t1.heightt(t1.root))
if(t1.bal(t1.root)):
    print("bal")
else:
    print("not")
print(t1.leafnode(t1.root))
print(t1.leafnodesum(t1.root))
print(t1.search(t1.root,90))
print(t1.depth(t1.root,4))
t1.leftview(t1.root,0,[])
t1.rightview(t1.root,0,[])
res=t1.top_view(t1.root,0,{})
print(res.values())



