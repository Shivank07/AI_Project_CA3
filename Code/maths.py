
class P:

    def __init__(self, x, y=None, z=None):
        try:
            i = iter(x)
            self.x = next(i)
            self.y = next(i)
            self.z = next(i)
        except TypeError:
            self.x = x
            self.y = y
            self.z = z
        if any(val is None for val in self):
            raise ValueError("It doesn't allow the None values: {self}")

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        return "Point" + str(self)

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return P(self.x * other, self.y * other, self.z * other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return P(self.y * other.z - self.z * other.y,
                     self.z * other.x - self.x * other.z,
                     self.x * other.y - self.y * other.x)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        raise IndexError("The Point index is not in range. Error!")

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def Count(self, val):
        return int(self.x == val) + int(self.y == val) + int(self.z == val)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __eq__(self, other):
        if isinstance(other, (tuple, list)):
            return self.x == other[0] and self.y == other[1] and self.z == other[2]
        return (isinstance(other, self.P) and self.x == other.x
                and self.y == other.y and self.z == other.z)

    def __ne__(self, other):
        return not (self == other)


class Matrix:

    def __init__(self, *args):
        if len(args) == 9:
            self.vals = list(args)
        elif len(args) == 3:
            try:
                self.vals = [x for y in args for x in y]
            except:
                self.vals = []
        else:
            self.__init__(*args[0])

        if len(self.vals) != 9:
            raise ValueError("Matrix requires 9 items, but recieved items : {args}")

    def __str__(self):
        return ("[{}, {}, {},\n"
                " {}, {}, {},\n"
                " {}, {}, {}]".format(*self.vals))

    def __repr__(self):
        return ("Matrix({}, {}, {},\n"
                "       {}, {}, {},\n"
                "       {}, {}, {})".format(*self.vals))

    def __eq__(self, other):
        return self.vals == other.vals

    def __add__(self, other):
        return Matrix(a + b for a, b in zip(self.vals, other.vals))

    def __sub__(self, other):
        return Matrix(a - b for a, b in zip(self.vals, other.vals))

    def __iadd__(self, other):
        self.vals = [a + b for a, b in zip(self.vals, other.vals)]
        return self

    def __isub__(self, other):
        self.vals = [a - b for a, b in zip(self.vals, other.vals)]
        return self

    def __mul__(self, other):
        if isinstance(other, P):
            return P(other.dot(P(row)) for row in self.rows())
        elif isinstance(other, Matrix):
            return Matrix(P(row).dot(P(col)) for row in self.rows() for col in other.cols())

    def rows(self):
        yield self.vals[0:3]
        yield self.vals[3:6]
        yield self.vals[6:9]

    def cols(self):
        yield self.vals[0:9:3]
        yield self.vals[1:9:3]
        yield self.vals[2:9:3]
