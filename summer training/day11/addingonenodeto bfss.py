def bfs(d,n):
    vi=[]
    q=[n]
    while(q):
        for i in d[q[0]]:
            if(i not in q and i not in vi):
                q.append(i)
        vi.append(q.pop(0))
        print(vi[-1])
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8,9],9:[2]}
l=[]
bfs(d,5)