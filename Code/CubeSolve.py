import sys
import time
import Code
from Code.maths import P

D = False

class Solver:

    def __init__(self, c):
        self.cube = c
        self.colors = c.colors()
        self.moves = []

        self.left_P  = self.cube.f_P(self.cube.left_color())
        self.right_P = self.cube.f_P(self.cube.right_color())
        self.up_P    = self.cube.f_P(self.cube.up_color())
        self.down_P  = self.cube.f_P(self.cube.down_color())

    def solve(self):
        if D: print(self.cube)
        self.cross()
        if D: print('Cube Cross:\n', self.cube)
        self.cross_corner()
        if D: print('Cube Corners:\n', self.cube)
        self.second_layer()
        if D: print('Second layer of the cube:\n', self.cube)
        self.back_face()
        if D: print('Last layer edges of the cube\n', self.cube)
        self.last_layer_corners_Pos()
        if D: print('Last layer corners position of the cube\n', self.cube)
        self.last_layer_corners_represent()
        if D: print('Last layer corners representation of cube\n', self.cube)
        self.last_layer_edge()
        if D: print('Solved Cube\n', self.cube)

    def mv(self, move_str):
        self.moves.extend(move_str.split())
        self.cube.seq(move_str)

    def cross(self):
        if D: print("Cube Cross")
        fl_P = self.cube.f_P(self.cube.front_color(), self.cube.left_color())
        fr_P = self.cube.f_P(self.cube.front_color(), self.cube.right_color())
        fu_P = self.cube.f_P(self.cube.front_color(), self.cube.up_color())
        fd_P = self.cube.f_P(self.cube.front_color(), self.cube.down_color())

        self._cross_l_or_r(fl_P, self.left_P, self.cube.left_color(), "L L", "E L Ei Li")
        self._cross_l_or_r(fr_P, self.right_P, self.cube.right_color(), "R R", "Ei R E Ri")

        self.mv("Z")
        self._cross_l_or_r(fd_P, self.down_P, self.cube.left_color(), "L L", "E L Ei Li")
        self._cross_l_or_r(fu_P, self.up_P, self.cube.right_color(), "R R", "Ei R E Ri")
        self.mv("Zi")

    def _cross_l_or_r(self, edge_P, face_P, face_color, mv_1, mv_2):
        if (edge_P.Pos == (face_P.Pos.x, face_P.Pos.y, 1)
                and edge_P.colors[2] == self.cube.front_color()):
            return
            
        undo_mv = None
        if edge_P.Pos.z == 0:
            Pos = P(edge_P.Pos)
            Pos.x = 0  # pick the UP or DOWN face
            cw, cc = Code.cube.get_rotate_face(Pos)

            if edge_P.Pos in (Code.cube.LEFT + Code.cube.UP, Code.cube.RIGHT + Code.cube.DOWN):
                self.mv(cw)
                undo_mv = cc
            else:
                self.mv(cc)
                undo_mv = cw
        elif edge_P.Pos.z == 1:
            Pos = P(edge_P.Pos)
            Pos.z = 0
            cw, cc = Code.cube.get_rotate_face(Pos)
            self.mv("{0} {0}".format(cc))
            if edge_P.Pos.x != face_P.Pos.x:
                undo_mv = "{0} {0}".format(cw)

        assert edge_P.Pos.z == -1
        c = 0
        while (edge_P.Pos.x, edge_P.Pos.y) != (face_P.Pos.x, face_P.Pos.y):
            self.mv("B")
            c += 1
            if c == 10:
                raise Exception("Unsolvable cube\n" + str(self.cube))
        if undo_mv:
            self.mv(undo_mv)
        if edge_P.colors[0] == face_color:
            self.mv(mv_1)
        else:
            self.mv(mv_2)

    def cross_corner(self):
        if D: print("Cross Corners of Cube")
        fld_P = self.cube.f_P(self.cube.front_color(), self.cube.left_color(), self.cube.down_color())
        flu_P = self.cube.f_P(self.cube.front_color(), self.cube.left_color(), self.cube.up_color())
        frd_P = self.cube.f_P(self.cube.front_color(), self.cube.right_color(), self.cube.down_color())
        fru_P = self.cube.f_P(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())

        self.frd_corner(frd_P, self.right_P, self.down_P, self.cube.front_color())
        self.mv("Z")
        self.frd_corner(fru_P, self.up_P, self.right_P, self.cube.front_color())
        self.mv("Z")
        self.frd_corner(flu_P, self.left_P, self.up_P, self.cube.front_color())
        self.mv("Z")
        self.frd_corner(fld_P, self.down_P, self.left_P, self.cube.front_color())
        self.mv("Z")

    def frd_corner(self, corner_P, right_P, down_P, front_color):
        if corner_P.Pos.z == 1:
            Position = P(corner_P.Pos)
            Position.x = Position.z = 0
            cw, cc = Code.cube.get_rotate_face(Position)
            c = 0
            undo_mv = cc
            while corner_P.Pos.z != -1:
                self.mv(cw)
                c += 1

            if c > 1:
                for _ in range(c):
                    self.mv(cc)
                c = 0
                while corner_P.Pos.z != -1:
                    self.mv(cc)
                    c += 1
                undo_mv = cw
            self.mv("B")
            for _ in range(c):
                self.mv(undo_mv)
                
        while (corner_P.Pos.x, corner_P.Pos.y) != (right_P.Pos.x, down_P.Pos.y):
            self.mv("B")
        if corner_P.colors[0] == front_color:
            self.mv("B D Bi Di")
        elif corner_P.colors[1] == front_color:
            self.mv("Bi Ri B R")
        else:
            self.mv("Ri B B R Bi Bi D Bi Di")

    def second_layer(self):
        rd_P = self.cube.f_P(self.cube.right_color(), self.cube.down_color())
        ru_P = self.cube.f_P(self.cube.right_color(), self.cube.up_color())
        ld_P = self.cube.f_P(self.cube.left_color(), self.cube.down_color())
        lu_P = self.cube.f_P(self.cube.left_color(), self.cube.up_color())

        self.middle_layer_ld(ld_P, self.cube.left_color(), self.cube.down_color())
        self.mv("Z")
        self.middle_layer_ld(rd_P, self.cube.left_color(), self.cube.down_color())
        self.mv("Z")
        self.middle_layer_ld(ru_P, self.cube.left_color(), self.cube.down_color())
        self.mv("Z")
        self.middle_layer_ld(lu_P, self.cube.left_color(), self.cube.down_color())
        self.mv("Z")

    def middle_layer_ld(self, ld_P, left_color, down_color):
        if ld_P.Pos.z == 0:
            count = 0
            while (ld_P.Pos.x, ld_P.Pos.y) != (-1, -1):
                self.mv("Z")
                count += 1

            self.mv("B L Bi Li Bi Di B D")
            for _ in range(count):
                self.mv("Zi")

        assert ld_P.Pos.z == -1

        if ld_P.colors[2] == left_color:
            while ld_P.Pos.y != -1:
                self.mv("B")
            self.mv("B L Bi Li Bi Di B D")
        elif ld_P.colors[2] == down_color:
            while ld_P.Pos.x != -1:
                self.mv("B")
            self.mv("Bi Di B D B L Bi Li")
        else:
            raise Exception("ERROR!!")

    def back_face(self):
        self.mv("X X")   # rotation of BACK to FRONT

        def S1():
            return (self.cube[0, 1, 1].colors[2] == self.cube.front_color() and
                    self.cube[-1, 0, 1].colors[2] == self.cube.front_color() and
                    self.cube[0, -1, 1].colors[2] == self.cube.front_color() and
                    self.cube[1, 0, 1].colors[2] == self.cube.front_color())

        def S2():
            return (self.cube[0, 1, 1].colors[2] == self.cube.front_color() and
                    self.cube[-1, 0, 1].colors[2] == self.cube.front_color())

        def S3():
            return (self.cube[-1, 0, 1].colors[2] == self.cube.front_color() and
                    self.cube[1, 0, 1].colors[2] == self.cube.front_color())

        def S4():
            return (self.cube[0, 1, 1].colors[2] != self.cube.front_color() and
                    self.cube[-1, 0, 1].colors[2] != self.cube.front_color() and
                    self.cube[0, -1, 1].colors[2] != self.cube.front_color() and
                    self.cube[1, 0, 1].colors[2] != self.cube.front_color())

        c = 0
        while not S1():
            if S4() or S2():
                self.mv("D F R Fi Ri Di")
            elif S3():
                self.mv("D R F Ri Fi Di")
            else:
                self.mv("F")
            c += 1
            if c == 10:
                raise Exception("Unsolvable cube\n" + str(self.cube))

        self.mv("Xi Xi")

    def last_layer_corners_Pos(self):
        self.mv("X X")

        mv_1 = "Li Fi L D F Di Li F L F F "  # swaps 1 and 2
        mv_2 = "F Li Fi L D F Di Li F L F "  # swaps 1 and 3

        c1 = self.cube.f_P(self.cube.front_color(), self.cube.right_color(), self.cube.down_color())
        c2 = self.cube.f_P(self.cube.front_color(), self.cube.left_color(), self.cube.down_color())
        c3 = self.cube.f_P(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())
        c4 = self.cube.f_P(self.cube.front_color(), self.cube.left_color(), self.cube.up_color())

        if c4.Pos == P(1, -1, 1):
            self.mv(mv_1 + "Zi " + mv_1 + " Z")
        elif c4.Pos == P(1, 1, 1):
            self.mv("Z " + mv_2 + " Zi")
        elif c4.Pos == P(-1, -1, 1):
            self.mv("Zi " + mv_1 + " Z")
        assert c4.Pos == P(-1, 1, 1)

        if c2.Pos == P(1, 1, 1):
            self.mv(mv_2 + mv_1)
        elif c2.Pos == P(1, -1, 1):
            self.mv(mv_1)
        assert c2.Pos == P(-1, -1, 1)

        if c3.Pos == P(1, -1, 1):
            self.mv(mv_2)
        assert c3.Pos == P(1, 1, 1)
        assert c1.Pos == P(1, -1, 1)

        self.mv("Xi Xi")

    def last_layer_corners_represent(self):
        self.mv("X X")

        def S1():
            return (self.cube[ 1,  1, 1].colors[1] == self.cube.front_color() and
                    self.cube[-1, -1, 1].colors[1] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[0] == self.cube.front_color())

        def S2():
            return (self.cube[-1,  1, 1].colors[1] == self.cube.front_color() and
                    self.cube[ 1,  1, 1].colors[0] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[1] == self.cube.front_color())

        def S3():
            return (self.cube[-1, -1, 1].colors[1] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[1] == self.cube.front_color() and
                    self.cube[-1,  1, 1].colors[2] == self.cube.front_color() and
                    self.cube[ 1,  1, 1].colors[2] == self.cube.front_color())

        def S4():
            return (self.cube[-1,  1, 1].colors[1] == self.cube.front_color() and
                    self.cube[-1, -1, 1].colors[1] == self.cube.front_color() and
                    self.cube[ 1,  1, 1].colors[2] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[2] == self.cube.front_color())

        def S5():
            return (self.cube[-1,  1, 1].colors[1] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[0] == self.cube.front_color())

        def S6():
            return (self.cube[ 1,  1, 1].colors[1] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[1] == self.cube.front_color() and
                    self.cube[-1, -1, 1].colors[0] == self.cube.front_color() and
                    self.cube[-1,  1, 1].colors[0] == self.cube.front_color())

        def S7():
            return (self.cube[ 1,  1, 1].colors[0] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[0] == self.cube.front_color() and
                    self.cube[-1, -1, 1].colors[0] == self.cube.front_color() and
                    self.cube[-1,  1, 1].colors[0] == self.cube.front_color())

        def S8():
            return (self.cube[ 1,  1, 1].colors[2] == self.cube.front_color() and
                    self.cube[ 1, -1, 1].colors[2] == self.cube.front_color() and
                    self.cube[-1, -1, 1].colors[2] == self.cube.front_color() and
                    self.cube[-1,  1, 1].colors[2] == self.cube.front_color())

        mv_1 = "Ri Fi R Fi Ri F F R F F "
        mv_2 = "R F Ri F R F F Ri F F "

        while not S8():
            if S1(): self.mv(mv_1)
            elif S2(): self.mv(mv_2)
            elif S3(): self.mv(mv_2 + "F F " + mv_1)
            elif S4(): self.mv(mv_2 + mv_1)
            elif S5(): self.mv(mv_1 + "F " + mv_2)
            elif S6(): self.mv(mv_1 + "Fi " + mv_1)
            elif S7(): self.mv(mv_1 + "F F " + mv_1)
            else:
                self.mv("F")

        # rotate the cube corners to their accurate locations
        bru_corner = self.cube.f_P(self.cube.front_color(), self.cube.right_color(), self.cube.up_color())
        while bru_corner.Pos != P(1, 1, 1):
            self.mv("F")

        self.mv("Xi Xi")

    def last_layer_edge(self):
        self.mv("X X")

        br_edge = self.cube.f_P(self.cube.front_color(), self.cube.right_color())
        bl_edge = self.cube.f_P(self.cube.front_color(), self.cube.left_color())
        bu_edge = self.cube.f_P(self.cube.front_color(), self.cube.up_color())
        bd_edge = self.cube.f_P(self.cube.front_color(), self.cube.down_color())

        def S1():
            return (bu_edge.colors[2] != self.cube.front_color() and
                    bd_edge.colors[2] != self.cube.front_color() and
                    bl_edge.colors[2] != self.cube.front_color() and
                    br_edge.colors[2] != self.cube.front_color())

        def S2():
            return (bu_edge.colors[2] == self.cube.front_color() or
                    bd_edge.colors[2] == self.cube.front_color() or
                    bl_edge.colors[2] == self.cube.front_color() or
                    br_edge.colors[2] == self.cube.front_color())


        repeat_mv = "R R F D Ui R R Di U F R R"
        h_pattern_move = "Ri S Ri Ri S S Ri Fi Fi R Si Si Ri Ri Si R Fi Fi "
        f_move = "Di Li " + h_pattern_move + " L D"

        if S1():
            self._handle_last_layer_S1(br_edge, bl_edge, bu_edge, bd_edge, repeat_mv, h_pattern_move)
        if S2():
            self._handle_last_layer_S2(br_edge, bl_edge, bu_edge, bd_edge, repeat_mv)

        def h_pattern1():
            return (self.cube[-1,  0, 1].colors[0] != self.cube.left_color() and
                    self.cube[ 1,  0, 1].colors[0] != self.cube.right_color() and
                    self.cube[ 0, -1, 1].colors[1] == self.cube.down_color() and
                    self.cube[ 0,  1, 1].colors[1] == self.cube.up_color())

        def h_pattern2():
            return (self.cube[-1,  0, 1].colors[0] == self.cube.left_color() and
                    self.cube[ 1,  0, 1].colors[0] == self.cube.right_color() and
                    self.cube[ 0, -1, 1].colors[1] == self.cube.front_color() and
                    self.cube[ 0,  1, 1].colors[1] == self.cube.front_color())

        def f_pattern():
            return (self.cube[Code.cube.FRONT + Code.cube.DOWN].colors[2] == self.cube.down_color() and
                    self.cube[Code.cube.FRONT + Code.cube.RIGHT].colors[2] == self.cube.right_color() and
                    self.cube[Code.cube.FRONT + Code.cube.DOWN].colors[1] == self.cube.front_color() and
                    self.cube[Code.cube.FRONT + Code.cube.RIGHT].colors[0] == self.cube.front_color())

        c = 0
        while not self.cube.is_solved():
            for _ in range(4):
                if f_pattern():
                    self.mv(f_move)
                    if self.cube.is_solved():
                        return
                else:
                    self.mv("Z")

            if h_pattern1():
                self.mv(h_pattern_move)
            elif h_pattern2():
                self.mv("Z " + h_pattern_move + "Zi")
            else:
                self.mv(repeat_mv)
            c += 1
            if c == 10:
                raise Exception("Unsolvable cube:\n" + str(self.cube))

        self.mv("Xi Xi")


    def _handle_last_layer_S1(self, br_edge, bl_edge, bu_edge, bd_edge, repeat_mv, h_move):
        if D: print("Handle the last layer of S1")
        def check_edge_lr():
            return self.cube[Code.cube.LEFT + Code.cube.FRONT].colors[2] == self.cube.left_color()

        c = 0
        while not check_edge_lr():
            self.mv("F")
            c += 1
            if c == 4:
                raise Exception("Error: Failed to handle first layer of S1")

        self.mv(h_move)

        for _ in range(c):
            self.mv("Fi")


    def _handle_last_layer_S2(self, br_edge, bl_edge, bu_edge, bd_edge, repeat_mv):
        if D: print("Handling the last layer of S2")
        def cor_edge():
            P = self.cube[Code.cube.LEFT + Code.cube.FRONT]
            if P.colors[2] == self.cube.front_color() and P.colors[0] == self.cube.left_color():
                return P
            P = self.cube[Code.cube.RIGHT + Code.cube.FRONT]
            if P.colors[2] == self.cube.front_color() and P.colors[0] == self.cube.right_color():
                return P
            P = self.cube[Code.cube.UP + Code.cube.FRONT]
            if P.colors[2] == self.cube.front_color() and P.colors[1] == self.cube.up_color():
                return P
            P = self.cube[Code.cube.DOWN + Code.cube.FRONT]
            if P.colors[2] == self.cube.front_color() and P.colors[1] == self.cube.down_color():
                return P

        c = 0
        while True:
            edge = cor_edge()
            if edge == None:
                self.mv(repeat_mv)
            else:
                break

            c += 1

            if c % 3 == 0:
                self.mv("Z")

            if c == 12:
                raise Exception("Unsolvable cube:\n" + str(self.cube))

        while edge.Pos != P(-1, 0, 1):
            self.mv("Z")

        assert self.cube[Code.cube.LEFT + Code.cube.FRONT].colors[2] == self.cube.front_color() and \
               self.cube[Code.cube.LEFT + Code.cube.FRONT].colors[0] == self.cube.left_color()


if __name__ == '__main__':
    D = True
    c = Code.main.Cube_Solve("DLURRDFFUBBLDDRBRBLDLRBFRUULFBDDUFBRBBRFUDFLUDLUULFLFR")
    print("Solving the Cube:\n", c)
    orig = Code.main.Cube_Solve(c)
    solver = Solver(c)
    solver.solve()

    print(f"{len(solver.moves)} Moves: {' '.join(solver.moves)}")

    check = Code.main.Cube_Solve(orig)
    check.seq(" ".join(solver.moves))
    assert check.is_cubesolved()
