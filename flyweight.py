class Circle:
    def __init__(self, color):
        self.color = color
        self.x = 0
        self.y = 0
        self.radius = 0

    def draw(self):
        print(f"Circle: Draw() [Color: {self.color}, x: {self.x}, y: {self.y}, radius: {self.radius}]")

class CircleFactory:
    _circle_map = {}

    @staticmethod
    def get_circle(color):
        circle = CircleFactory._circle_map.get(color)
        if circle is None:
            circle = Circle(color)
            CircleFactory._circle_map[color] = circle
            print(f"Creating circle of color: {color}")
        return circle


colors = ["Red", "Green", "Blue", "White", "Black"]
for i in range(20):
    circle = CircleFactory.get_circle(colors[i % len(colors)])
    circle.x = i * 10
    circle.y = i * 20
    circle.radius = 100
    circle.draw()
