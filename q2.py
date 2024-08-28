s1=input("enter string")

r=s1.split(' ')
rw=[]
for i in r:
    rw.append(i[::-1])

r=' '.join(rw)    
print(r)
