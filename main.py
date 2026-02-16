#foodprice1=7
#foodprice2=10
#totalcost=foodprice1+foodprice2
#print (totalcost)

#------------------------------------------------
#calculateTotal

def add(foodprice1,foodprice2):
    foodprice1 = input('First choice')
    foodprice2 = input('Second choice')
    answer=foodprice1+foodprice2
    return answer

result=float()
#print(result)

#------------------------------------------------
#applyDiscount
if result>=10:
    answer=result*0.9
else:
    answer=result
#print(answer)

#------------------------------------------------
#displayReceipt
username = input('What is your name? ')
print(username)
print(answer)