from user import *
from datetime import *
from food import *
from bank import *

class Order:
    def __init__(self, ID, iduser:User):
        self.ID = ID
        self.iduser = iduser
        self.date = datetime.now()


    def __str__(self):
        return f"{self.ID} {self.iduser} {self.table}"
    

    def detail_list(self):
        list_order = []
        for x in Order_food.list_order_food:
            if self == x.idorder:
                list_order.append(x)
        return list_order


    def status_to_pay(self):
        paytotal = 0
        x = self.detail_list()
        for i in x:
            paytotal += i.price
        self.paytotal = paytotal
        self.status = "paing"

    def status_to_payed(self, paytype):
        paytype = 0
        self.status_to_pay()
        self.paytype = paytype


class Order_food:
    list_order_food = []
    def __init__(self, ID, idfood:Food, idorder:Order, num):
        self.ID = ID
        self.idfood = idfood
        self.idorder = idorder
        self.num = num
        self.price = num * idfood.price
        Order_food.list_order_food.append(self)

    def __str__(self):
        return f"{self.idfood.name} {self.num} {self.price}"

obj_order = Order(4, obj_user)
obj_order_1 = Order(5, obj_user_2)
obj_order_2 = Order(6, obj_user_3)
obj_order_food = Order_food(7, obj_food, obj_order, 2)
obj_order_food_1 = Order_food(8, obj_food_1, obj_order_1, 1)
obj_order_food_2 = Order_food(9, obj_food_2, obj_order_2, 3)
obj_order_food_2 = Order_food(10, obj_food_1, obj_order_2, 5)
obj_order_food_2 = Order_food(11, obj_food_2, obj_order_1, 4)

print(Order_food.list_order_food)
x = obj_order_2.detail_list()
for i in x:
    print(i)
obj_order_2.status_to_pay()
print(obj_order_2.paytotal)

