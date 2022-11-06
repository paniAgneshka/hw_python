import math
def make_ndim_vector_class(n):
    class Vector(object):
        def __init__(self, *coord):
            self.dim = n
            self.coord = []
            if len(coord) == n:
                for x in coord:
                    self.coord.append(x)
            else:
                print("The class constructor requires n arguments - coordinates of vector!")
                self.coord = [None for i in range(n)]

        
        def get_length(self):
            length = 0
            for x in self.coord:
                length += x**2
            return math.sqrt(length)
        
        def show(self):
            print(self.coord)
        
        def __add__(self, other):
            if self.dim == other.dim: 
                return Vector(*(self.coord[i] + other.coord[i] for i in range(self.dim)))
            else:
                print("Vectors have different dimensions")
                return Vector(*(None for i in range(n)))
    return Vector


Vector3 = make_ndim_vector_class(3)
v = Vector3(1, 2, 3)
u = Vector3(3, 4, 5)
Vector2 = make_ndim_vector_class(2)
z = Vector2(1, 0)
print("Length of U =")
print(u.get_length())
print("V =")
v.show()
print("U + V =")
(u + v).show()
print("U + Z =")
(u + z).show()

