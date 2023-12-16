class Type:
    def __init__(self,ID, fname, Ename):
        self.ID = ID
        self.fname = fname
        self.ename = Ename

    
    def __str__(self):
        return f"{self.fname} {self.ename}"
    
class Food:
    list_food = []
    def __init__(self, ID, name, price, IDtype:Type):
        self.ID = ID
        self.name = name
        self.price = price
        self.IDtype = IDtype

    def add_food(self):
        Food.list_food.append(self.name)
        return Food.list_food

    def __str__(self):
        return f"{self.IDtype} {self.name} {self.price}\n"

class Base:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} {self.price}"
    
class Base_food:
    def __init__(self, ID, IDfood:Food, IDbase:Base, size):
        self.ID = ID
        self.IDfood = IDfood
        self.IDbase = IDbase
        self.size = size


    def __str__(self) -> str:
        return f"{self.ID} {self.size}"
        

obj_type = Type(1, "سرد", "cold")
obj_type_1 = Type(2, "گرم", "hot")
obj_type_2 = Type(3, "نوشیدنی", "drink")
obj_food = Food(4, "kabab", 45000, obj_type)
obj_food_1 = Food(5, "rice", 120000, obj_type_1)
obj_food_2 = Food(6, "estake", 300000, obj_type_2)