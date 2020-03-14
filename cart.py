def Main():
	cart =[]
	cart.append(dict(item="Water", price=2, qty=2))
	cart.append(dict(item="Papaya", price=3, qty=1))
	cart.append(dict(item="Stake", price=36, qty=4))

	t = Template("$qty x $item = $price)
	total = 0
	print("Cart:")
	for data in cart:
		print(t.substitute(data))
		total+=data["price"]
	print("Total:"+str(total))
if __name__=='__main__':
	Main()
