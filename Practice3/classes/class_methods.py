# CLASS METHODS AND INSTANCE METHODS
# Instance methods work with object data using self.

# Example 1: Instance methods
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} added to account.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn from account.")
        else:
            print("Not enough money.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


account = BankAccount("Yeskendir", 10000)

account.show_balance()
account.deposit(5000)
account.withdraw(3000)
account.show_balance()


# Example 2: Method that returns value
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rectangle = Rectangle(5, 4)
print("Rectangle area:", rectangle.calculate_area())


# Example 3: Class method with @classmethod
class University:
    university_name = "KBTU"

    @classmethod
    def show_university_name(cls):
        print("University:", cls.university_name)


University.show_university_name()


# Example 4: Static method
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b


print("Static method result:", MathHelper.add(10, 20))