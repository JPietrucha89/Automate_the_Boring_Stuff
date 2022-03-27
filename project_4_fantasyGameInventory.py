#Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
import pprint

def displayInventory(dictParameter):
    if isinstance(dictParameter,dict): 
        print("Inventory:")
        totalNumberOfItems=0
        for k,v in dictParameter.items():
            print(v,k)
            totalNumberOfItems+=v
        print("Total number of items: ", totalNumberOfItems)
    else:
        return None

def addToInventory(dictParameter,listParameter):
    for item in listParameter:
        if item in dictParameter:
            dictParameter[item]=dictParameter[item]+1
        else:
            dictParameter.setdefault(item,1)

#main
inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inventory,dragonLoot)
displayInventory(inventory)