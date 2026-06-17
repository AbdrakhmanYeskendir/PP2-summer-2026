# METHOD OVERRIDING
# A child class can replace a method from the parent class.

# Example 1: Parent class
class Animal:
    def make_sound(self):
        print("Animal makes a sound.")


# Example 2: Child classes override the method
class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")


class Cat(Animal):
    def make_sound(self):
        print("Cat meows.")


animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()


# Example 3: Parent class
class User:
    def show_role(self):
        print("Role: regular user")


# Example 4: Child class with overridden method
class Admin(User):
    def show_role(self):
        print("Role: administrator")


user1 = User()
admin1 = Admin()

user1.show_role()
admin1.show_role()


# Example 5: Overriding but still using parent method
class PremiumUser(User):
    def show_role(self):
        super().show_role()
        print("Additional role: premium user")


premium_user = PremiumUser()
premium_user.show_role()