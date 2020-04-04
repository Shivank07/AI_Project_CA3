import random
import time
from Code.main import Cube_Solve
from Code.CubeSolve import Solver
from Code.opt import opt_mv

SOLVED_CUBE = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
Mv = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]


def random_mix():
    mix_mv = " ".join(random.choices(Mv, k=2))
    a = Cube_Solve(SOLVED_CUBE)
    a.seq(mix_mv)
    return a

def run():
    suc = 0
    fail = 0

    average_opt_moves = 0.0
    average_moves = 0.0
    average_time = 0.0
    while True:
        C = random_mix()
        solver = Solver(C)

        Start = time.time()
        solver.solve()
        dur = time.time() - Start

        if C.is_cubesolved():
            opt_moves = opt_mv(solver.moves)
            suc += 1
            average_moves = (average_moves * (suc - 1) + len(solver.moves)) / float(suc)
            average_time = (average_time * (suc - 1) + dur) / float(suc)
            average_opt_moves = (average_opt_moves * (suc - 1) + len(opt_moves)) / float(suc)
        else:
            fail += 1
            print("Failure ({suc + fail}): {C.flat_str()}")

        t = suc + fail
        if t == 1 or t % 100 == 0:
            pass_percent = 100 * suc / t
            print(f"{t}: {suc} Success ({pass_percent:0.3f}% Pass)"
                  f" avg_moves={average_moves:0.3f} avg_opt_moves={average_opt_moves:0.3f}"
                  f" avg_time={average_time:0.3f}s")


if __name__ == '__main__':
    solve.D = False
    run()
