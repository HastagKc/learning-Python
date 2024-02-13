# Oop pillar 

# class and object 
# Inheritance 
# Encapsulation 
# Polymorphism 

# class and object 
'''
classes are the blueprint for creating an objects. An object is an instance 
of a class. Class define attributes(data) and methods (functions) that operate 
on those attributes
'''

# creating class Of Car name 
class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def display_info(self):
        print(f'name: {self.name} model: {self.model}')


# creating object of Car types 
car1 = Car("Toyata", "Toyata-123")
car2 = Car("Honda", "Honda-522")

# accessing method 
car1.display_info()
car2.display_info()