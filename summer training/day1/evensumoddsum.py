s=input()
es=0
os=0
ds=0
for i in s:
    if int(i)%2==0:
        es=es+i
    elif int(i)%2!=0:
        os=os+i
    else:
        ds=ds+i
print(es)
        