l=[]
while 1:
    s=input()
    if s=='':
        break
    a=list(map(int,s.split(',')))
    l.append(a)
for i in l:
    print(", ".join(map(str,i)))