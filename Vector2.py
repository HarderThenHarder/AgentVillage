import math


class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        assert type(self) == type(other), "Vector2(type) must add the Vector2(type)"
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __sub__(self, other):
        assert type(self) == type(other), "Vector2(type) must sub the Vector2(type)"
        x = self.x - other.x
        y = self.y - other.y
        return Vector2(x, y)

    def __mul__(self, value):
        x = self.x * value
        y = self.y * value
        return Vector2(x, y)

    def __repr__(self):
        return "Vector2(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def dot(self, other):
        assert type(self) == type(other), "Vector2(type) must dot the Vector2(type)"
        return self.x * other.x + self.y * other.y

    def normalization(self):
        if self.__abs__():
            x = self.x / self.__abs__()
            y = self.y / self.__abs__()
        else:
            x = 0
            y = 0
        return Vector2(x, y)

    def copy(self):
        return Vector2(self.x, self.y)

    def get_distance_to(self, other):
        assert type(self) == type(other), "Vector2(type) must calculate with Vector2(type)"
        return math.hypot(self.x - other.x, self.y - other.y)
    
    def get_angel_to(self, other):
        assert type(self) == type(other), "Vector2(type) must calculate with Vector2(type)"
        return math.hypot(self.x - other.x, self.y - other.y)

    def get_xy(self):
        return self.x, self.y


if __name__ == '__main__':
    v1 = Vector2(1, 1)
    v2 = Vector2(2, 2)
    print(v1.get_distance_to(v2))
