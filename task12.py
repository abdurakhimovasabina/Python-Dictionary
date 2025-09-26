inventory = {
    "apple": 5, 
    "banana": 2
}

product = input("Yangi meva: ")
inventory[product] = inventory.get(product, 0)

print(inventory)
