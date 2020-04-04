import string
import textwrap
from Code.maths import Point, Matrix
import Code.maths

RIGHT = X_AXIS = Point(1, 0, 0)
LEFT           = Point(-1, 0, 0)
UP    = Y_AXIS = Point(0, 1, 0)
DOWN           = Point(0, -1, 0)
FRONT = Z_AXIS = Point(0, 0, 1)
BACK           = Point(0, 0, -1)

FACE = 'face'
EDGE = 'edge'
CORNER = 'corner'


# XY plane. CW:clockwise, CC:counter-clockwise.
rotate_XY_CW = Code.maths.Matrix(0, 1, 0,
                                  -1, 0, 0,
                                  0, 0, 1)
rotate_XY_CC = Code.maths.Matrix(0, -1, 0,
                                  1, 0, 0,
                                  0, 0, 1)

# XZ plane 
rotate_XZ_CW = Code.maths.Matrix(0, 0, -1,
                                  0, 1, 0,
                                  1, 0, 0)
rotate_XZ_CC = Code.maths.Matrix(0, 0, 1,
                                  0, 1, 0,
                                  -1, 0, 0)

# YZ plane
rotate_YZ_CW = Code.maths.Matrix(1, 0, 0,
                                  0, 0, 1,
                                  0, -1, 0)
rotate_YZ_CC = Code.maths.Matrix(1, 0, 0,
                                  0, 0, -1,
                                  0, 1, 0)


def get_rotate_face(face):
    if face == RIGHT:   return "R", "Ri"
    elif face == LEFT:  return "L", "Li"
    elif face == UP:    return "U", "Ui"
    elif face == DOWN:  return "D", "Di"
    elif face == FRONT: return "F", "Fi"
    elif face == BACK:  return "B", "Bi"
    return None


class P:

    def __init__(self, position, col):
        assert all(type(x) == int and x in (-1, 0, 1) for x in position)
        assert len(col) == 3
        self.position = position
        self.col = list(col)
        self._set_P_type()

    def __str__(self):
        color = "".join(c for c in self.col if c is not None)
        return f"({self.type}, {color}, {self.position})"

    def _set_P_type(self):
        if self.col.count(None) == 2:
            self.type = FACE
        elif self.col.count(None) == 1:
            self.type = EDGE
        elif self.col.count(None) == 0:
            self.type = CORNER
        else:
            raise ValueError(f"Must have 1, 2, or 3 colors - given colors={self.colors}")

    def rot(self, m):
        privious = self.position
        self.position = m * self.position
        rot = self.position - privious
        if not any(rot):
            return  
        if rot.count(0) == 2:
            rot += m * rot

        assert rot.count(0) == 1, (
            f" ERROR OCCOURED!"
            f"\nPrevious: {privious}"
            f"\nself.position: {self.position}"
            f"\nrot: {rot}"
        )

        i, j = (i for i, x in enumerate(rot) if x != 0)
        self.colors[i], self.colors[j] = self.col[j], self.col[i]


class Cube_Solve:
    def _cube(self, c):
        self.faces = [P(position=P(p.position), colors=p.colors) for p in c.faces]
        self.edges = [P(position=P(p.position), colors=p.colors) for p in c.edges]
        self.corners = [P(position=P(p.position), colors=p.colors) for p in c.corners]
        self.Ps = self.faces + self.edges + self.corners

    def _data(self):
        assert len(self.Ps) == 30
        assert all(p.type == FACE for p in self.faces)
        assert all(p.type == EDGE for p in self.edges)
        assert all(p.type == CORNER for p in self.corners)

    def __init__(self, cube_str)
        if isinstance(cube_str, Cube_Solve):
            self._cube(cube_str)
            return

        cube_str = "".join(x for x in cube_str if x not in string.space)
        assert len(cube_str) == 54
        self.faces = (
            P(position=RIGHT, colors=(cube_str[28], None, None)),
            P(position=LEFT,  colors=(cube_str[22], None, None)),
            P(position=UP,    colors=(None, cube_str[4],  None)),
            P(position=DOWN,  colors=(None, cube_str[49], None)),
            P(position=FRONT, colors=(None, None, cube_str[25])),
            P(position=BACK,  colors=(None, None, cube_str[31])))
        self.edges = (
            P(position=RIGHT + UP,    colors=(cube_str[16], cube_str[5], None)),
            P(position=RIGHT + DOWN,  colors=(cube_str[40], cube_str[50], None)),
            P(position=RIGHT + FRONT, colors=(cube_str[27], None, cube_str[26])),
            P(position=RIGHT + BACK,  colors=(cube_str[29], None, cube_str[30])),
            P(position=LEFT + UP,     colors=(cube_str[10], cube_str[3], None)),
            P(position=LEFT + DOWN,   colors=(cube_str[34], cube_str[48], None)),
            P(position=LEFT + FRONT,  colors=(cube_str[23], None, cube_str[24])),
            P(position=LEFT + BACK,   colors=(cube_str[21], None, cube_str[32])),
            P(position=UP + FRONT,    colors=(None, cube_str[7], cube_str[13])),
            P(position=UP + BACK,     colors=(None, cube_str[1], cube_str[19])),
            P(position=DOWN + FRONT,  colors=(None, cube_str[46], cube_str[37])),
            P(position=DOWN + BACK,   colors=(None, cube_str[52], cube_str[43])),
        )
        self.corners = (
            P(position=RIGHT + UP + FRONT,   colors=(cube_str[15], cube_str[8], cube_str[14])),
            P(position=RIGHT + UP + BACK,    colors=(cube_str[17], cube_str[2], cube_str[18])),
            P(position=RIGHT + DOWN + FRONT, colors=(cube_str[39], cube_str[47], cube_str[38])),
            P(position=RIGHT + DOWN + BACK,  colors=(cube_str[41], cube_str[53], cube_str[42])),
            P(position=LEFT + UP + FRONT,    colors=(cube_str[11], cube_str[6], cube_str[12])),
            P(position=LEFT + UP + BACK,     colors=(cube_str[9], cube_str[0], cube_str[20])),
            P(position=LEFT + DOWN + FRONT,  colors=(cube_str[35], cube_str[45], cube_str[36])),
            P(position=LEFT + DOWN + BACK,   colors=(cube_str[33], cube_str[51], cube_str[44])),
        )

        self.Ps = self.faces + self.edges + self.corners
        self._data()

    def is_cubesolved(self):
        def check_cube(colors):
            assert len(colors) == 9
            return all(c == colors[0] for c in colors)
        return (check_cube([P.col[2] for P in self._cube_face(FRONT)]) and
                check_cube([P.col[2] for P in self._cube_face(BACK)]) and
                check_cube([P.col[1] for P in self._cube_face(UP)]) and
                check_cube([P.col[1] for P in self._cube_face(DOWN)]) and
                check_cube([P.col[0] for P in self._cube_face(LEFT)]) and
                check_cube([P.col[0] for P in self._cube_face(RIGHT)]))

    def _cube_face(self, axis):
        assert axis.count(0) == 2
        return [p for p in self.Ps if p.position.dot(axis) > 0]

    def _cube_slice(self, plane):
        assert plane.count(0) == 1
        i = next((i for i, x in enumerate(plane) if x == 0))
        return [p for p in self.Ps if p.position[i] == 0]

    def _rotate_cube_face(self, face, Matrix):
        self._rotate_Ps(self._cube_face(face), Matrix)

    def _rotate_cube_slice(self, plane, Matrix):
        self._rotate_Ps(self._cube_slice(plane), Matrix)

    def _rotate_Ps(self, Ps, Matrix):
        for P in Ps:
            P.rotate(Matrix)

    def R(self):  self._rotate_cube_face(RIGHT, rotate_YZ_CW)
    def Ri(self): self._rotate_cube_face(RIGHT, rotate_YZ_CC)
    def L(self):  self._rotate_cube_face(LEFT, rotate_YZ_CC)
    def Li(self): self._rotate_cube_face(LEFT, rotate_YZ_CW)
    def D(self):  self._rotate_cube_face(DOWN, rotate_XZ_CC)
    def Di(self): self._rotate_cube_face(DOWN, rotate_XZ_CW)
    def U(self):  self._rotate_cube_face(UP, rotate_XZ_CW)
    def Ui(self): self._rotate_cube_face(UP, rotate_XZ_CC)
    def F(self):  self._rotate_cube_face(FRONT, rotate_XY_CW)
    def Fi(self): self._rotate_cube_face(FRONT, rotate_XY_CC)
    def B(self):  self._rotate_cube_face(BACK, rotate_XY_CC)
    def Bi(self): self._rotate_cube_face(BACK, rotate_XY_CW)
    def E(self):  self._rotate_cube_slice(X_AXIS + Z_AXIS, rotate_XZ_CC)
    def Ei(self): self._rotate_cube_slice(X_AXIS + Z_AXIS, rotate_XZ_CW)
    def M(self):  self._rotate_cube_slice(Y_AXIS + Z_AXIS, rotate_YZ_CC)
    def Mi(self): self._rotate_cube_slice(Y_AXIS + Z_AXIS, rotate_YZ_CW)
    def S(self):  self._rotate_cube_slice(X_AXIS + Y_AXIS, rotate_XY_CW)
    def Si(self): self._rotate_cube_slice(X_AXIS + Y_AXIS, rotate_XY_CC)
    def X(self):  self._rotate_Ps(self.Ps, rotate_YZ_CW)
    def Xi(self): self._rotate_Ps(self.Ps, rotate_YZ_CC)
    def Y(self):  self._rotate_Ps(self.Ps, rotate_XZ_CW)
    def Yi(self): self._rotate_Ps(self.Ps, rotate_XZ_CC)
    def Z(self):  self._rotate_Ps(self.Ps, rotate_XY_CW)
    def Zi(self): self._rotate_Ps(self.Ps, rotate_XY_CC)

    def seq(self, mv_str):
        moves = [getattr(self, name) for name in mv_str.split()]
        for mv in moves:
            mv()

    def f_P(self, *color):
        if None in color:
            return
        for p in self.Ps:
            if p.col.count(None) == 3 - len(color) \
                and all(c in p.colors for c in color):
                return p

    def get_P(self, x, y, z):
        pt = P(x, y, z)
        for p in self.Ps:
            if p.position == pt:
                return p

    def __getitem__(self, *args):
        if len(args) == 1:
            return self.get_P(*args[0])
        return self.get_P(*args)

    def __eq__(self, other):
        return isinstance(other, Cube_Solve) and self._color_list() == other._color_list()

    def __ne__(self, other):
        return not (self == other)

    def col(self):
        return set(c for P in self.Ps for c in P.colors if c is not None)

    def left_color(self): return self[LEFT].col[0]
    def right_color(self): return self[RIGHT].col[0]
    def up_color(self): return self[UP].col[1]
    def down_color(self): return self[DOWN].col[1]
    def front_color(self): return self[FRONT].col[2]
    def back_color(self): return self[BACK].col[2]

    def _color_list(self):
        right = [p.colors[0] for p in sorted(self._cube_face(RIGHT), key=lambda p: (-p.position.y, -p.position.z))]
        left  = [p.colors[0] for p in sorted(self._cube_face(LEFT),  key=lambda p: (-p.position.y, p.position.z))]
        up    = [p.colors[1] for p in sorted(self._cube_face(UP),    key=lambda p: (p.position.z, p.position.x))]
        down  = [p.colors[1] for p in sorted(self._cube_face(DOWN),  key=lambda p: (-p.position.z, p.position.x))]
        front = [p.colors[2] for p in sorted(self._cube_face(FRONT), key=lambda p: (-p.position.y, p.position.x))]
        back  = [p.colors[2] for p in sorted(self._cube_face(BACK),  key=lambda p: (-p.position.y, -p.position.x))]

        return (up + left[0:3] + front[0:3] + right[0:3] + back[0:3]
                   + left[3:6] + front[3:6] + right[3:6] + back[3:6]
                   + left[6:9] + front[6:9] + right[6:9] + back[6:9] + down)

    def flat_str(self):
        return "".join(x for x in str(self) if x not in string.space)

    def __str__(self):
        template = ("    {}{}{}\n"
                    "    {}{}{}\n"
                    "    {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "    {}{}{}\n"
                    "    {}{}{}\n"
                    "    {}{}{}")

        return "    " + template.format(*self._color_list()).strip()


if __name__ == '__main__':
    cube = Cube_Solve("    DLU\n"
                "    RRD\n"
                "    FFU\n"
                "BBL DDR BRB LDL\n"
                "RBF RUU LFB DDU\n"
                "FBR BBR FUD FLU\n"
                "    DLU\n"
                "    ULF\n"
                "    LFR")
    print(cube)
