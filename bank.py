from termcolor import colored
from user import *


class Bank(User):
    def __init__(self, ID, balance, password):
        super().__init__(ID, name, phon, adress=None)
        self.balance = balance
        self.password = password

    def money_in(self, money, password):
        self.money = money
        bank_password = 3345
        if password == bank_password:
            self.balance += self.money
            print(colored("account balance has been update: ","green"),self.balance)
        else:
            print(colored("your password is wrong...","yellow"))
    
    def money_out(self, money, password):
        self.money = money
        bank_password = 3345
        if password == bank_password:
            if self.money > self.balance:
                print(colored("insufficient funds => your balance is: ","blue"),self.balance)
            
            else:
                self.balance -= self.money
                print(colored("account balance has been update: ","red"),self.balance)
        else:
            print(colored("your password is wrong...","yellow"))
    
    def show_balance(self, password):
        bank_password = 3345
        if password == bank_password:
            print(colored("account balance is: ","green"),self.balance)
        else:
            print(colored("youe password is wrong...","yellow"))


print("your information:")
id = int(input("\tpleas enter the youe ID: "))
name = input("pleas enter your name: ")
phon = input("pleas enter your phonnumber: ")
balance = int(input("\tpleas enter your account balance: "))
money = int(input("\tpleas enter your money: "))
password = int(input("\tpleas enter the your password: "))

obj2 = Bank(id, balance, password)

while True:
    print("1.creat account \n 2.get balance \n 3.money_in \n 4.money_out")
    choice = int(input("select any option"))
    if choice == 1:
        print(obj_user.show())
        print(obj_user_2.show())
        print(obj_user_3.show())

    elif choice == 2:
        obj2.show_balance(password)

    elif choice == 3:
        obj2.money_in(money, password)

    elif choice == 4:
        obj2.money_out(money, password)

    else:
        print(colored("your choice is wrong...","yellow"))
        break