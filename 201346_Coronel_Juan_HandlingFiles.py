products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def get_product(code):
	return products[code]
def get_property(code, property):
	return(products[code][property]
def main(): 
    total = 0
    receipt = {}
    
    while(True):
        user_input = input("Input:")
        if user_input != "/":
            item = user_input.split(",")
            code = item[0]
            item2 = int(item[1])
            if code in receipt.keys():
                receipt[code]+= item2
            else:
                receipt[code]= item2
        elif user_input == "/":
            break
        
    with open("receipt.txt","w") as f:             
        f.write(F'''
==
CODE\t\t\t\tNAME\t\t\t\tQUANTITY\t\t\t\tSUBTOTAL''')
        
        for i in products.keys():
            if i in receipt.keys():
                name = get_property(i,"name")
                price = get_property(i,"price") * receipt[i]
                total += price
                f.write(F'''\n{i}\t\t\t{name}\t\t\t\t{receipt[i]}\t\t\t\t\t{price}''')
        f.write(F'''\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t\t\t{total}
==
''')
