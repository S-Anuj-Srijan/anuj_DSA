class Person:
    def __init__(self,name, age ):
        self.age=age
        self.name=name 

    def greet(self):
        print(f"greeting mrs {self.name}")

a = Person("anuj",42)
a.greet()
