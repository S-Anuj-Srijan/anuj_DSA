"""QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
 number by turning over as few cards as possible. Write a function to help Bob locate the card."""

test = [{"input":{"cards":[1,2,3,4,5,6,7,8,9],"query":6},"output":5},
    {"input":{"cards":[1,2,1,1,3,4,5,3,4],"query":4},"output":5},
    {"input":{"cards":[1,2,3,4,5,7],"query":6},"output":-1},
    {"input":{"cards":[],"query":6},"output":-1}]


def linear_search(cards,query):
    count=0
    for i in cards:

        if i == query :
            return count
        count+=1
    return -1



for i in test: 
    result=linear_search(cards=i["input"]["cards"],query=i["input"]["query"])
    print(result)
    print(result == i["output"])

    