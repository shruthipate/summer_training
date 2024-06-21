class Node:
    def __init__(self):
        self.d= {}
        self.flag=0
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, str):
        t = self.root
        for i in str:
            if(i not in t.d):
                t.d[i] = Node()
            t = t.d[i]
        t.flag=1
    def search(self,str):
        t = self.root
        for i in str:
            if (i not in t.d):
                return False
            t = t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def prefix(self,str):
        t=self.root
        for i in str:
            if (i not in t.d):
                return False
            t=t.d[i]
        return True
    
        
t1= Trie()
t1.insert("world")
t1.insert("word")
t1.insert("woo")
print(t1.search("world"))
print(t1.prefix("wo"))
n=int(input())
for i in range(n):
    a,b=input().split()
    if(a=='1'):
        t1.insert(b)
    if(a=='2'):
        print(t1.search(b))
    if(a=='3'):
        print(t1.prefix(b))