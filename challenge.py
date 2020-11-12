#given the list of shoes in a shop and the number of customers and the price each paid for the shoes
shoeList = [2,3,4,5,6,8,7,6,5,18]
customers = 6
size_price= {6:[55,45,55],4:[40],18:[60],10:[50]}
sales= 0

for shoes in size_price:
    if shoes not in shoeList:
        print('size {},is not available right now'. format(shoes))
        
for shoes in set(shoeList):
    if shoes not in size_price:
        print('size {}, is still available on the shelf'.format(shoes))
    else:
        for i in range(shoeList.count(shoes)):
            sales+=(size_price[shoes][i])
            print('size {}, is sold for #{}'.format(shoes, size_price[shoes][i]))
print ('Total amount recovered from the sales is #%d'%(sales))
