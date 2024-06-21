class node:
    def __init__(self,d):
        self.data=d
        self.next=None
class lis:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data)%2==0:
                s=s+t.data
            t=t.next
        print(s)
    def front(self,x):
        t=node(x)
        t.next=self.head
        self.head=t
    def searching(self,x):
        t=self.head
        while(t!=None):
            if x==t.data:
                return "found"
            t=t.next
        return "no"
    def me(self):
        s=self.head
        f=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        print(s.data)
    def me(self):
        s=self.head
        f=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        if(f==None):
            print("even")
        else:
            print("odd")
    def longeststr(self):
        lens=1
        max_length=0
        t=self.head
        while(t.next!=None):
            if(t.data==(t.next.data)-1):
                lens=lens+1
            else:
                if(lens>max_length):
                    max_length=lens
                    lens=1
            t=t.next
        if(lens>max_length):
            max_length=lens
        print(max_length)
    def pairs(self):
        t=self.head
        while(t.next!=None):
            t1=t.next
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
    def bubble(self):
        c=0
        T=self.head
        p=None
        while(T.next!=None):
            f=0
            t=self.head
            while(t.next!=p):
                if(t.data>t.next.data):
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
                c=c+1
            if(f==0):
                break
            p=t
            T=T.next
        return c
                    
        
        
        
l1=lis()
l1.head=node(50)
l1.addback(21)
l1.addback(22)
l1.addback(40)
l1.addback(80)
l1.front(70)
l1.addeven()
print(l1.searching(0))
l1.me()
l1.longeststr()
l1.pairs()
l1.display()
print()
print(l1.bubble())
print()
l1.display()




            
        
        
        