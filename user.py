class User:
    def __init__(self, ID, name, phon, adress = None):
        self.ID = ID
        self.name = name
        self.phon = phon 
        self.adress = adress


    def show(self):
        return f"name is: {self.name} age is: {self.age} and gender is: {self.gender}"

    
obj_user = User(1, "kosar", "09197820884")
obj_user_2 = User(2, "mobina", "09636473747")
obj_user_3 = User(3, "nima", "096366383747")

