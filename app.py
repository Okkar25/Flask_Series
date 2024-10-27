class Car:
    def __init__(self,color,wheels,model,brand):
        
        self.color=color
        self.wheels=wheels
        self.model=model
        self.brand=brand

    def drive(self):
        print("car is driving")

    def turn(self):
        print("car is turning")

    def reverse(self):
        print("car is reversing")


car1=Car('white',4,2023,'Toyota')
car2=Car('Black',5,2024,'Mushibishi')

print(car1.color)
print(car2.color)

car1.drive()
car2.turn()