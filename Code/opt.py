from Code import main
#CW : Clockwise & CC : Counter Clockwise
X_rotate_CW = {
    'U': 'F',
    'B': 'U',
    'D': 'B',
    'F': 'D',
    'E': 'Si',
    'S': 'E',
    'Y': 'Z',
    'Z': 'Yi',
}
Y_rotate_CW = {
    'B': 'L',
    'R': 'B',
    'F': 'R',
    'L': 'F',
    'S': 'Mi',
    'M': 'S',
    'Z': 'X',
    'X': 'Zi'
}
Z_rotate_CW = {
    'U': 'L',
    'R': 'U',
    'D': 'R',
    'L': 'D',
    'E': 'Mi',
    'M': 'E',
    'Y': 'Xi',
    'X': 'Y',
}
X_rotate_CC = {v: k for k, v in X_rotate_CW.items()}
Y_rotate_CC = {v: k for k, v in Y_rotate_CW.items()}
Z_rotate_CC = {v: k for k, v in Z_rotate_CW.items()}


def get_rot(rotation):
    if rotation == 'X': return X_rotate_CW
    elif rotation == 'Xi': return X_rotate_CC
    elif rotation == 'Y': return Y_rotate_CW
    elif rotation == 'Yi': return Y_rotate_CC
    elif rotation == 'Z': return Z_rotate_CW
    elif rotation == 'Zi': return Z_rotate_CC


def _invert(mv):
    if mv.endswith('i'):
        return mv[:1]
    return mv + 'i'


def repeat_optimize(mv):
    change = False
    i = 0
    while i < len(mv) - 2:
        if mv[i] == mv[i+1] == mv[i+2]:
            mv[i:i+3] = [_invert(mv[i])]
            change = True
        else:
            i += 1
    if change:
        repeat_optimize(mv)


def undo_optimize(mv):
    change = False
    i = 0
    while i < len(mv) - 1:
        if _invert(mv[i]) == mv[i+1]:
            mv[i:i+2] = []
            change = True
        else:
            i += 1
    if change:
        undo_optimize(mv)


def _unrot(rot, mv):
    rot_t = get_rot(rot)
    result = []
    for move in mv:
        if move in rot_t:
            result.append(rot_t[move])
        elif _invert(move) in rot_t:
            result.append(_invert(rot_t[_invert(move)]))
        else:
            result.append(move)
    return result


def no_cube_rot_optimize(mv):
    rotation = {'X', 'Y', 'Z', 'Xi', 'Yi', 'Zi'}
    change = False
    i = 0
    while i < len(mv):
        if mv[i] not in rotation:
            i += 1
            continue

        for j in reversed(range(i + 1, len(mv))):
            if mv[j] == _invert(mv[i]):
                mv[i:j+1] = _unrot(mv[i], mv[i+1:j])
                change = True
                break
        i += 1
    if change:
        no_cube_rot_optimize(mv)


def opt_mv(mv):
    result = list(mv)
    no_cube_rot_optimize(result)
    repeat_optimize(result)
    undo_optimize(result)
    return result


if __name__ == '__main__':
    test_seq_1 = ("Li Li E L Ei Li B Ei R E Ri Z E L Ei Li Zi U U Ui Ui Ui B U B B B Bi "
                  "Ri B R Z U U Ui Ui Ui B U B B B Ri B B R Bi Bi D Bi Di Z Ri B B R Bi "
                  "Bi D Bi Di Z B B Bi Ri B R Z B L Bi Li Bi Di B D B Bi Di B D B L Bi Li "
                  "Z B B B Bi Di B D B L Bi Li Z B Bi Di B D B L Bi Li Z B B B L Bi Li Bi "
                  "Di B D Z X X F F D F R Fi Ri Di Xi Xi X X Li Fi L D F Di Li F L F F Zi "
                  "Li Fi L D F Di Li F L F F Z F Li Fi L D F Di Li F L F Li Fi L D F Di "
                  "Li F L F F Xi Xi X X Ri Fi R Fi Ri F F R F F F R F Ri F R F F Ri F F F "
                  "F Ri Fi R Fi Ri F F R F F F R F Ri F R F F Ri F F Xi Xi X X R R F D Ui "
                  "R R Di U F R R R R F D Ui R R Di U F R R Z Z Z Z Z Z R R F D Ui R R Di "
                  "U F R R Z Z Z Z R R F D Ui R R Di U F R R Z Z Z Z Z Ri S Ri Ri S S Ri "
                  "Fi Fi R Si Si Ri Ri Si R Fi Fi Zi Xi Xi")
    mv = test_seq_1.split()
    print("{len(moves)} Moves: {' '.join(moves)}")

    opt = opt_mv(mv)
    print("{len(opt)} Moves: {' '.join(opt)}")

    orig = main.Cube_Solve("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
    c= main.Cube_Solve(orig)
    d=main.Cube_Solve(orig)

    c.seq(" ".join(mv))
    d.seq(" ".join(opt))
    print(c, '\n')
    print(d)
    assert c == d
