s="leet**co*de"
st=[]
for i in s:
    if(i!='*'):
        st.append(i)
    else:
        st.pop()
print(''.join(st))