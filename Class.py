class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        def introduce(self):
            print("Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")
            
            # creating an instance of the person class
            person1 = Person("Bryson", 34, "Man")
            
            # calling the introduce method to display the person's information
            person1.introduce()
            