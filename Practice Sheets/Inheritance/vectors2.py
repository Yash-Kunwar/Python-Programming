class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}î + {self.vec[1]}ĵ + {self.vec[2]}k̂"

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)