class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str): 
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def prefix_s(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        return True
    def all_preffix(self,str):
        def fun(t,s):
            if t.flag==1:
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
            
        t=self.root
        s=""
        for i in str:
            if(i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return 
        fun(t,s)
    def longest_prefix(self, str):
        t = self.root
        longest = ""
        cur = ""
        for i in str:
            if i in t.d:
                cur += i
                t = t.d[i]
                if t.flag == 1:
                    longest = cur
            else:
                break
        return longest
t1=tries()
t1.insert("word")
t1.insert("world")
print(t1.search("word"))
print(t1.prefix_s("as"))
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search(s))
    if(a=='3'):
        print(t1.prefix_s(s))
    if(a=='4'):
        t1.all_preffix(s)
    if(a=='5'):
        print(t1.longest_prefix(s))
        


















