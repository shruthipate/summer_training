def match(l1,l2):
    def evenodd(l1,l2,i,j,res):
        if i>=len(l1):
            return res
        if j>=len(l2):
            return evenodd(l1,l2,i+1,0,res)
        if l1[i]%2==0 and l2[j]%2!=0:
            res.append(l1[i]+l2[j])
        return evenodd(l1,l2,i,j+1,res)
    return evenodd(l1,l2,0,0,[])

    
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
res=match(l1,l2)
print(res)
    
    