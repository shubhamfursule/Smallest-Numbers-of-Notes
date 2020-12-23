def Smallest_num(n):
    l=[1,2,5,10,50,100]
    max1=l[0]
    for i in range(0,len(l)):
        if  max1<n and l[i]<=n:
            max1=l[i]
            
    return max1
def Smallest_num_notes(n2):
    count=0
    while n2:
        a=Smallest_num(n2)
        count+=1
        n2-=a
    return count
l1=[]
for T in range(int(input())):
    n1=int(input()) 
    l1.append(Smallest_num_notes(n1))
for k in l1:
    print(k)