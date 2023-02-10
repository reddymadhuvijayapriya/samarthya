class car:
    def __init__(self,name,price,model):
        self.name=name
        self.price=price
        self.model=model
    def myfunc(self):
        print(f"this is {self.name} and it's price is is {self.price} and it's model is {self.model} ")
    def __str__(self):
        return "name: "+ self.name + ", price: " + str(self.price) + ", model: " + str(self.model)
p1=car("audi",100,3)
p1.myfunc()
print(p1)