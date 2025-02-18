a = [1,2,3,5,6,7,8,9,0]
b=[1,2,3,5,6,7,8,9,0]
#to insert a valeu 4 in 3 index we first have to make space 
a.append(a[-1])
count=len(a)-2
#this loop runs for n times in the worst case scenario thus the notation 0(n)
for i in reversed(a[0:len(a)-2]):
    a[count]=i
    count=count-1
    if count==3:
        a[3]=4
        break
#u can also use .insert() method in python 
b.insert(3,4)
print(b)
print(a)



    
