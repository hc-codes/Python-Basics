s=input()
sub=[]
vowels="aeiou"
for i in range(-1,len(s)):
    if(i==len(s)-1):
        sub.append(s)
        print(s)
    for j in range(i+1,len(s)):
        if(i==-1 ):
            sub.append(s[j])
            print(s[j],end=" , ")
        else:
            sub.append(s[i]+s[j])
            print(s[i]+s[j],end=" , ")
            break
print("\n",sub)
c=0
for i in sub:
    for j in i:
        if j in vowels:
            c=c+1
print("count = ",c)
count=0
for i in range(len(s)):
    if s[i] in vowels:
        count+=(len(s)-i)*(i+1)
print("count = ",count)