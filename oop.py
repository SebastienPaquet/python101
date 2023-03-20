class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)




studentA = Student("Quagmire",(80,70,90,94,86))
studentB = Student("Peter",(60,70,50,64,66))

print(studentA.name)
print(studentA.grades)
print(studentA.average_grade())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} ans"
    
    def __repr__(self) -> str:
        return f"<Person('{self.name}', {self.age})>"
    
bob = Person("Bob",33)
print(bob)


class Store:
    def __init__(self,name):
        self.name=name
        self.items=[]
    
    def add_item(self, name, price):
        dict = {"name":name, "price":price}
        self.items.append(dict)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item["price"] for item in self.items])
    
    @classmethod
    def a_class_method(cls):
        print(f"Called a_class_method of {cls}")

    @staticmethod
    def a_static_method():
        print(f"Called a static method")

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + "- franchise")

    @staticmethod
    def store_details(store) -> 'str':
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format( store.name, int(store.stock_price()) )

store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
store2.add_item("Mouse", 80)

Store.franchise(store2)
print(Store.store_details(store2))

Store.a_class_method()

Store.a_static_method()


class Book:
    TYPES = ("hardcover", "paperback")      #class properties

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weight: {self.weight}g>"

book = Book("Brave New World","paperback",400)
print(book)

print(Book.TYPES)