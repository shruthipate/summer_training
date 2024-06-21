s="is2 sentence4 this1 a3"
x=s.split()
re=[0]*len(x)
for i in x:
    re[(int(i[-1]-1))]=i[:-1]
print(''.join(re))
    
    
    

    