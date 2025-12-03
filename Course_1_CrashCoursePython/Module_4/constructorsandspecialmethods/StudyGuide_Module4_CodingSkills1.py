#Basically this program scans a single statement of a shopping item and a price. Like "Furry Coat 499" and it stores all the text into one single string and then the number in it's own separate string. Then afterwards, It creates a sentence using both pieces of information, for example, "The price of this Furry Coat is 499 dollars.". And so it would have to insert those pieces of information into the string. 
def sales_price(item_and_price):
    item = ""
    price = ""

    item_or_price = item_and_price.split()

    for x in item_or_price:
        if x.isalpha():
            item += x + " "
        else:
            price = x

    item = item.strip()
    return "{} is on sale for ${}!".format(item, price)

print(sales_price("Warm Winter Coat 199.99"))

