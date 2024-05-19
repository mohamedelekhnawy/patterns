class Product:
    def use(self):
        pass

class ConcreteProductA(Product):
    def use(self):
        print("Using Product A")

class ConcreteProductB(Product):
    def use(self):
        print("Using Product B")

class Creator:
    def factory_method(self):
        pass

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

creator_a = ConcreteCreatorA()
product_a = creator_a.factory_method()
product_a.use()  # Using Product A
