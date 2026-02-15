#foodprice1=7
#foodprice2=10
#totalcost=foodprice1+foodprice2
#print (totalcost)

#------------------------------------------------
#calculateTotal
def add(foodprice1,foodprice2):
    answer=foodprice1+foodprice2
    return answer

result=add(3,7)
print(result)

#------------------------------------------------
#applyDiscount
if result>=10:
    answer=result*0.9
else:
    answer=result
print(answer)

#------------------------------------------------