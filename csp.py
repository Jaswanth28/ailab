def dis(ans,val):
    l = []
    for i in val:
        if i!='o':
            l.append(val[i])
    l2=[]
    for i in ans:
        if ans[i] in l:
            return False
        l2.append(ans[i])
    return len(l2)==len(list(set(l2)))

val = {'t':0,'w':0,'o':0}
inp="two"
ou="four"
ans={'f':0,'o':0,'u':0,'r':0}
for t in range(1,10):
    val['t']=t
    for w in range(1,10):
        if w==t:
            continue
        val['w']=w
        for o in range(1,10):
            if o==w or o==t:
                continue
            val['o']=o
            ans['r'] = (val['o']*2)%10
            ans['u'] = (val['o']*2)//10+val['w']*2
            ans['o'] = ans['u']//10+val['t']*2
            ans['u']%=10
            ans['f'] = ans['o']//10
            ans['o']%=10
            if ans['o']==val['o'] and ans['f']>0 and dis(ans,val):
                two=""
                four=""
                for i in inp:
                    two+=str(val[i])
                for i in ou:
                    four+=str(ans[i])
                print(f"two({two}) + two({two}) ==four({four})")
