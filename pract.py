def dispstr(s1,s2,string1):
    ltocomm=[]
    ltouncom=[]
    ns1=sorted(s1)
    ns2=sorted(s2)
    
    for i in set(s1):
        if i in set(s2):
            ltocomm.append(i)
            
    for i in set(s2):
        if i in set(s1):
            ltocomm.append(i)
    
    for i in set(s1):
        if i not in set(s2):
            ltouncom.append(i)
            
    for i in set(s2):
        if i not in set(s1):
            ltouncom.append(i)
    print("uncomm:",set(ltouncom))
    print("comm:",set(ltocomm))
s1="today"
s2="tdoayyi"
print(dispstr(s1,s2,s2))    
     
