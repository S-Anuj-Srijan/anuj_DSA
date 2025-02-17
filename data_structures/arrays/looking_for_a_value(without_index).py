a=[1,2,3,4,5,6,7,8,9,0]
count=0
for i in a : 
    if i ==0 : 
        print(f"i found in {count}")
    count+=1

'''the big o notation for this code is 0(n) as if u dont know the index in the worst case scenario u have to search the whole list0'''
'''note: if index is known the big 0 notation is 0(1)'''