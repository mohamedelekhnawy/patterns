
class Car:
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def show(self):
        print("Car parts: " + ", ".join(self._parts))


class CarBuilder:
    def build_engine(self):
        pass

    def build_tires(self):
        pass

    def build_color(self):
        pass

    def get_car(self):
        pass


class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.add("Sports Engine")

    def build_tires(self):
        self.car.add("Sports Tires")

    def build_color(self):
        self.car.add("Red Color")

    def get_car(self):
        return self.car

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.build_engine()
        self._builder.build_tires()
        self._builder.build_color()


builder = SportsCarBuilder()
director = Director(builder)
director.construct_car()

car = builder.get_car()
car.show()  # Car parts: Sports Engine, Sports Tires, Red Color
