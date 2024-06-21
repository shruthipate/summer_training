class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def searching(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            if(t.data==x or t1.data==x):
                return 1
            t=t.next
            t1=t1.prev
        if(t.data==x):
            return 1
        else:
            return 0
    def findleng(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if(t==t1):
            print("Odd")
        else:
            print("Even")
        
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    def palindrome(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            if(t.data!=t1.data):
                return "no"
            t=t.next
            t1=t1.prev
        return "pal"
    def halfprint(self):
        f=self.head
        s=self.head
        while(f!=None):
            f=f.next.next
            s=s.next
        t=self.head
        t1=s
        while(t1!=None):
            t.data,t1.data=t1.data,t.data
            t=t.next
            t1=t1.next
    def eos(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.eos(t.next,es,os)
        
            
l1=dll()
l1.addback(90)
l1.addback(11)
l1.addback(20)
l1.addfront(30)
l1.findleng()
print(l1.searching(30))
l1.display()
print(l1.palindrome())
l1.halfprint()
l1.display()
print(l1.eos(l1.head,0,0))
l1.display

        