# read prdlist.csv file
products = []
with open('prdlist.csv', 'r', encoding='utf-8') as list:
    for line in list:
        prdname, price = line.strip().split(',')
        products.append([prdname, price])
		#s = line.strip().split(',')
		#prdname = s[0]
		#price = s[1]
        #products.append([name, price])
print(products)


products = []
while True:
    prdname = input('Input a product name: ')
    if prdname == 'Exit':
	    break
    price = input('Input the price of product: ')
    price = int(price)
    products.append([prdname, price])
print(products)
    
for p in products:
    print('The price of', p[0], 'is', p[1])
	
with open('prdlist.csv', 'w', encoding='utf-8') as list:
    list.write('商品,價目\n')
    for p in products:
	    list.write(p[0] + ',' + str(p[1]) + '\n')