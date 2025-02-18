a = [1,2,3,4,4,5,6,7,8,9,0]
b= [1,2,3,4,4,5,6,7,8,9,0]
a[3]="x"
count=0
for i in a :
    if count > 3:
        a[count-1]=i
    count+=1

print(a)
#the big0 notation for this is 0(n) as there is swapping involved 
#.remove() also can be removed 
b.remove(4)
print(b)
#note tht this operation can only be done to dynamic arrays not static arrays 

