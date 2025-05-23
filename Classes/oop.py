# 4 PILLARS
# encapsulation
# inheritance
# abstraction
# polymorphism


# encapsulation is data's security, hiding the data from the outside world.
# abstraction is simplicity, hiding the complexity of the system.
# inheritance is the ability to create a new class from an existing class. take properties from the parent class and add new properties to the child class.
# polymorphism is an object that behave differently in different situations. it is the ability to take many forms. it is the ability to use a single interface to represent different types of objects.


# encapsulation
# class Animal():
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age


#     def get(self , _age):
#         return self.__age
    

#     def set(self , _age):
#         self.__age = _age
#         return self.__age

#     def show(self):
#         print(f"Name: {self.name} Age: {self.__age}")
    

# cat = Animal("cat", 2)
# cat.show()
# cat.set(5)
# cat.show()

# difference between encapsulation and abstraction is that encapsulation is a way of restricting access to certain details of an object, while abstraction is a way of simplifying complex systems by hiding unnecessary details. Encapsulation is about protecting the data, while abstraction is about simplifying the interface.

# inheritance

class Animal():
    def __init__(self):
        self.name = "FATHER"

    def show(self):
        print(f"name ")
 

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "child"



Dog.show(Dog)