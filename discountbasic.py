#price and discount question if amount greater than 1000 then 10% discount otherwise no discount ask user total quantity


qu=int(input())
amount=qu*100
if(amount>1000):
    amount=amount-((amount*10)/100)
    print(amount)
else:
    print(amount)