import random

class Stock():

    # donne un attribut de classe (on aurait aussi pu
    # initialiser un compteur à 0 et l'augmenter de 1 à 
    # chaque instanciation d'objet via un +=1 dans le __init__)
    #instances_counter = itertools.count().next
    instances_counter = 0

    def __init__(self):
        self.id = Stock.instances_counter
        self.inventory = []
        self.inventory_value = 0
        Stock.instances_counter += 1
    
    def add_shoes(self):
        for element in Shoe.list_shoes_created:
            if element.inventoried == False:
                self.inventory.append(element)
                element.inventory = True
                element.stock = self.id
                
            else:
                continue
        self.set_value()

    def delete_shoes(self, shoe_id):
        for item in self.inventory:
            if item.id == shoe_id:
                item.sold = True
                self.inventory.remove(item)
        self.set_value()

    def set_value(self):
        self.inventory_value = sum([item.price for item in self.inventory])
        

class Shoe():

    instances_counter = 0
    list_shoes_created = []

    def __init__(self, pointure=42, color=None, brand=None, price=random.randrange(10,300)):
        # si pointure n'est pas précisée à l'instanciation mettra 42 par défaut.
        self.id = Shoe.instances_counter
        self.pointure = pointure
        self.color = color
        self.brand = brand
        self.price = price
        self.inventoried = False
        self.sold = False
        self.stock = None
        Shoe.list_shoes_created.append(self)
        Shoe.instances_counter += 1
        #self.color=color
        if type(self.pointure) is not int or self.pointure < 14 or self.pointure > 46:
            self.pointure = input("merci de rentrer un nombre entier compris entre 14 et 46")

        #if type(self.pointure) is not int or self.pointure < 14 or self.pointure > 46:
            #raise ValueError('Shoe pointure attribute only accepts integers between 14 and 46')
       # if type(self.color) is not string:
            #raise ValueError("Shoe color must be a string")

        

my_stock = Stock()

shoe1 = Shoe()
shoe2 = Shoe(color="red")
shoe3 = Shoe(pointure=24)

Shoe.list_shoes_created
shoe3.id

my_stock.add_shoes()
my_stock.inventory

my_stock.delete_shoes(shoe_id=1)
print(my_stock.inventory_value)
print(shoe1.price, shoe2.price)
my_stock