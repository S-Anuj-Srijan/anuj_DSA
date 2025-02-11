"""QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
 number by turning over as few cards as possible. Write a function to help Bob locate the card."""

test=[{"input":{'cards':[1, 3, 5, 7, 9],"target":5},"output":2},
      {"input":{'cards':[2, 4, 6, 8, 10],"target":2},"output":0},
      {"input":{'cards':[10, 20, 30, 40, 50],"target":50},"output":4},
      {"input":{'cards':[],"target":50},"output":-1},
      {"input":{'cards':[10, 20, 30, 50,60,50,40,40],"target":50},"output":3},
      {"input":{'cards':[10, 20, 30, 40, 60],"target":50},"output":-1}]

def look_for_card(cards,target):
    lo, hi = 0,len(cards)-1
    while lo<=hi:
        mid = (lo + hi)//2
        if cards[mid]==target:
            return mid 
        elif cards[mid]>target:
            hi = mid-1
        elif cards[mid]<target:
            lo = mid+1
    return -1 

for i in test :
    result=look_for_card(cards=i["input"]["cards"],target=i["input"]["target"])
    print(result)
    print(result==i["output"])


    