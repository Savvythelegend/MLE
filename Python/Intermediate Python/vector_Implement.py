class Vector():
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
# since the addtion of two vector returns another vector 
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z) 
        return result
        
    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result  
        
    def __str__(self):
        return f"{self.x}i+ {self.y}j+ {self.z}k"

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

print(v1 + v2)
print(v1 * v2)

# write a class to create a 3d vector 

class twod_vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return f"({self.x}i, {self.y}j)"

# objectoverloading 

    # def __add__(self, other):
    #     return twod_vector(self.x + other.x, self.y + other.y)

    # def __sub__(self, other):
    #     return twod_vector(self.x - other.x, self.y - other.y)

    # def __mul__(self, other):
    #     return self.x * other.x + self.y * other.y

    # def __str__(self):
    #     return f"({self.x}, {self.y})"


class threed_vector(twod_vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def show(self):
        return f"({self.x}i, {self.y}j, {self.z}k)"

v2d1 = twod_vector(1, 2)
v2d2 = threed_vector(3, 4, 5)
print(v2d1.show())
print(v2d2.show())
