import random
import time
from functools import wraps
from typing import Any, Callable, Dict, Generator, List, Tuple

from tqdm.auto import tqdm


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"||{func.__name__:^20} || Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

class ProblemGenerator:
    def __init__(self, default_samples: List[Tuple[Any, Any]],
                 sampler: Callable[..., Any],
                 max_samples: int = -1,
                 level: str = "",
                 name: str = "",
                 float_authorized_error: float = -1,
                 **kwargs: Any) -> None:
        self.default_samples = default_samples
        self.sampler = sampler
        self.max_samples = max_samples
        self.level = level
        self.name = name
        self.float_authorized_error = float_authorized_error
        self.kwargs = kwargs

    def sample(self, sample_test_cases: bool, at_maximum: bool = False) -> Generator[Any, None, None]:
        if sample_test_cases:
            for param, solution in tqdm(self.default_samples):
                yield param, solution
        else:
            for param in tqdm(range(self.max_samples), total=self.max_samples):
                yield self.sampler(at_maximum, **self.kwargs), None

    def WrongMessage(self, i: int, result: Any) -> str:
        msg: str = f"Wrong solution to {self.level} - {self.name} -- sample test case #{i+1}."
        msg += f"\nExpected: {self.default_samples[i][1]}"
        msg += f"\nGot: {result}"
        return msg

    def evaluate(self, func: Callable[..., Any], sample_test_cases: bool = False, at_maximum: bool = False) -> None:
        for i, (sample, solution) in enumerate(self.sample(sample_test_cases, at_maximum)):
            result = measure_time(func)(*sample)
            if self.float_authorized_error != -1 and isinstance(result, float) and isinstance(solution, float):
                assert (abs(result - solution) <= self.float_authorized_error) or (solution is None), self.WrongMessage(i, result)
            else:
                assert (result == solution) or (solution is None), self.WrongMessage(i, result)


def Warmup_ABCs_sampler(MAX_VALUE: int) -> Tuple[int, int, int]:
    A = random.randint(1, MAX_VALUE)
    B = random.randint(1, MAX_VALUE)
    C = random.randint(1, MAX_VALUE)

    return A, B, C

def Warmup_AllWrong_sampler(MAX_N: int, VALUES: str) -> Tuple[int, str]:
    N = random.randint(1, MAX_N)
    C = ''.join(random.choice(VALUES) for _ in range(N))

    return N, C

def Warmup_Battleship_sampler(MAX_R: int, MAX_C: int, MAX_G: int) -> Tuple[int, int, List[List[int]]]:
    R = random.randint(1, MAX_R)
    C = random.randint(1, MAX_C)
    G = [[random.randint(1, MAX_G) for _ in range(C)] for _ in range(R)]

    return R, C, G

def Level1_Cafetaria_Sampler(MAX_N: int, MAX_M: int):
    N = random.randint(1, MAX_N)
    K = random.randint(1, N)
    M = random.randint(1, min(MAX_M, N))
    S = [random.randint(1, N) for _ in range(M)]

    return N, K, M, S

def Level1_DirectorOfPhotography_Sampler(MAX_N: int, VALUES: str) -> Tuple[int, str, int, int]:
    N = random.randint(1, MAX_N)
    C = ''.join(random.choice(VALUES) for _ in range(N))
    X = random.randint(1, N)
    Y = random.randint(X, N)

    return N, C, X, Y

def Level1_Kaitenzushi_Sampler(MAX_N: int, MAX_D: int) -> Tuple[int, List[int], int]:
    N = random.randint(1, MAX_N)
    K = random.randint(1, N)
    D = [random.randint(1, MAX_D) for _ in range(N)]

    return N, D, K

def Level1_Rotary_Lock_1_Sampler(MAX_N: int, MAX_M: int) -> Tuple[int, int, List[int]]:
    N = random.randint(1, MAX_N)
    M = random.randint(1, MAX_M)
    C = [random.randint(1, N) for _ in range(M)]

    return N, M, C

def Level1_Scoreboard_Inference_1_Sampler(MAX_N: int, MAX_S: int) -> Tuple[int, List[int]]:
    N = random.randint(1, MAX_N)
    S = [random.randint(1, MAX_S) for _ in range(N)]
    return N, S

def Level1_Stack_Stabilization_1_Sampler(MAX_N: int, MAX_R: int) -> Tuple[int, List[int]]:
    N = random.randint(1, MAX_N)
    R = [random.randint(1, MAX_R) for _ in range(N)]
    return N, R

def Level1_Uniform_Integers_Sampler(MAX: int) -> Tuple[int, int]:
    A = random.randint(1, MAX)
    B = random.randint(A, MAX)

    return A, B


def Level2_Director_Of_Photography_Sampler(MAX_N: int, VALUES: str) -> Tuple[int, str, int, int]:
    N = random.randint(1, MAX_N)
    C = ''.join(random.choice(VALUES) for _ in range(N))
    X = random.randint(1, N)
    Y = random.randint(X, N)
    return N, C, X, Y

def Level2_Hops_Sampler(MAX_N: int, MAX_F: int) -> Tuple[int, int, List[int]]:
    N = random.randint(1, MAX_N)
    F = random.randint(1, MAX_F)

    range_ = range(N)
    random.shuffle(list(range_))

    return N, F, list(range_[::N])

def Level2_Missing_Mail_Sampler(MAX_N: int, MAX_V: int, MAX_C: int) -> Tuple[int, List[int], int, float]:
    N = random.randint(1, MAX_N)
    V = [random.randint(0, MAX_V) for _ in range(N)]
    C = random.randint(1, MAX_C)
    S = random.random()

    return N, V, C, S

def Level2_Portals_Sampler(MAX: int, VALUES: str) -> Tuple[int, int, List[List[str]]]:
    R = random.randint(1, MAX)
    C = random.randint(1, MAX)
    G = [[random.choice(VALUES) for _ in range(C)] for _ in range(R)]

    i,j = random.randint(0, R-1), random.randint(0, C-1)
    G[i][j] = 'S'

    return R, C, G

def Level2_Rabbit_Hole_1_Sampler(MAX_N: int) -> Tuple[int, List[int]]:
    N = random.randint(2, MAX_N)
    L: List[int] = []
    for i in range(1, N+1):
        val = random.randint(1, N+1)
        while val == i:
            val = random.randint(1, N+1)
        L.append(val)

    return N, L

def Level2_Rotary_Lock_2_Sampler(MAX_N: int, MAX_M: int) -> Tuple[int, int, List[int]]:
    N = random.randint(3, MAX_N)
    M = random.randint(1, MAX_M)
    C = [random.randint(1, N+1) for _ in range(M)]
    return N, M, C

def Level2_Scoreboard_Inference_2_Sampler(MAX_N: int, MAX_S: int) -> Tuple[int, List[int]]:
    N = random.randint(1, MAX_N)
    S = [random.randint(1, MAX_S) for _ in range(N)]
    return N, S

def Level2_Tunnel_Time_Sampler(MAX_C: int, MAX_N: int, MAX_K: int) -> Tuple[int, int, List[int], List[int], int]:
    C = random.randint(3, MAX_C)
    N = random.randint(1, min(MAX_N, MAX_C//2))
    AB = list(range(1, C+1))
    random.shuffle(AB)
    AB_ = sorted(AB[:2*N])
    A = AB_[::2]
    B = AB_[1::2]
    order = list(range(N))
    random.shuffle(order)
    A_ = [A[i] for i in order]
    B_ = [B[i] for i in order]
    K = random.randint(1, MAX_K)

    return C, N, A_, B_, K


def Level3_Boss_Fight_Sampler(MAX_N: int, MAX_H: int, MAX_D: int, MAX_B: int) -> Tuple[int, List[int], List[int], int]:
    N = random.randint(2, MAX_N)
    H = [random.randint(1, MAX_H) for _ in range(N)]
    D = [random.randint(1, MAX_D) for _ in range(N)]
    B = random.randint(1, MAX_B)
    return N, H, D, B

def Level3_Rabbit_Hole_2_Sampler(MAX_N: int, MAX_M: int) -> Tuple[int, int, List[int], List[int]]:
    N = random.randint(2, MAX_N)
    M = random.randint(1, MAX_M)
    A: List[int] = [random.randint(1, N) for _ in range(M)]
    B: List[int] = []
    for j in range(M):
        val = random.randint(1, N)
        while val == A[j]:
            val = random.randint(1, N)
    return N, M, A, B

def Level3_Slippery_Trip_Sampler(MAX_R: int, MAX_C: int, MAX_RC: int, VALUES: str) -> Tuple[int, int, List[List[str]]]:
    R = random.randint(2, MAX_R)
    C = random.randint(2, MAX_RC//R)
    G = [[random.choice(VALUES) for _ in range(C)] for _ in range(R)]

    return R, C, G


def Level3_Stack_Stabilization_2_Sampler(MAX_N: int, MAX_R: int, MAX_AB: int) -> Tuple[int, List[int], int, int]:
    N = random.randint(1, MAX_N)
    R = [random.randint(1, MAX_R) for _ in range(N)]
    A = random.randint(1, MAX_AB)
    B = random.randint(1, MAX_AB)

    return N, R, A, B

def Level4_Conveyor_Chaos_Sampler(MAX_N: int, MAX_H: int, MAX_AB: int) -> Tuple[int, List[int], List[int], List[int]]:
    N = random.randint(1, MAX_N)
    H = [random.randint(1, MAX_H) for _ in range(N)]
    A = [random.randint(0, MAX_AB-1) for _ in range(N)]
    B = [random.randint(A[j]+1, MAX_AB) for j in range(N)]

    return N, H, A, B

def Level4_Mathematical_Art_Sampler(MAX_N: int, MAX_L: int, DS: str) -> Tuple[int, List[int], str]:
    N = random.randint(1, MAX_N)
    L = [random.randint(1, MAX_L) for _ in range(N)]
    D = ''.join(random.choice(DS) for _ in range(N))
    return N, L, D


WARMUPS: Dict[str, Any] = {
    "ABCs" : {
        "default_samples" :
            [
                ((1,2,3),6),
                ((100,100,100),300),
                ((85,16,93),194)
            ],
        "sampler" : Warmup_ABCs_sampler,
        "max_samples" : 10,
        "level" : "Warmup",
        "name" : "ABCs",
        "MAX_VALUE" : 100
    },
    "All Wrong" : {
        "default_samples" :
            [
                ((3, 'ABA'), 'BAB'),
                ((5, 'BBBBB'), 'AAAAA')
            ],
        "sampler" : Warmup_AllWrong_sampler,
        "max_samples" : 10,
        "level" : "Warmup",
        "name" : "All Wrong",
        "MAX_N" : 100,
        "VALUES" : 'AB'
    },
    "Battleship" : {
        "default_samples" :
            [
                ((2,3,[[0,0,1],[1,0,1]]), 0.5000000000),
                ((2,2,[[1,1],[1,1]]), 1.0000000000)
            ],
        "sampler" : Warmup_Battleship_sampler,
        "max_samples" : 10,
        "level" : "Warmup",
        "name" : "Battleship",
        "MAX_R" : 100,
        'MAX_C' : 100,
        'MAX_G' : 1,
        'float_authorized_error' : 10**-6
    }
}

LEVEL1: Dict[str, Any] = {
    "Cafetaria" : {
        "default_samples" :
            [
               ((10,1,2,[2,6]), 3),
               ((15,2,3,[11,6,14]),1)
            ],
        "sampler" : Level1_Cafetaria_Sampler,
        "max_samples" : 10,
        "level" : "Level 1",
        "name" : "Cafetaria",
        "MAX_N" : 10**15,
        "MAX_M" : 500000
    },
    "Director Of Photography" : {
        "default_samples" :
            [
               ((5,'APABA', 1, 2), 1),
               ((5, 'APABA', 2, 3), 0),
               ((8, '.PBAAP.B', 1, 3), 3)
            ],
        "sampler" : Level1_DirectorOfPhotography_Sampler,
        "max_samples" : 10,
        "level" : "Level 1",
        "name" : "Director Of Photography",
        "MAX_N" : 200,
        "VALUES" : 'PAB.'
    },
    "Kaitenzushi" : {
        "default_samples" :
            [
                ((6,[1,2,3,3,2,1],1), 5),
                ((6,[1,2,3,3,2,1],2), 4),
                ((7,[1,2,1,2,1,2,1],2), 2)
            ],
        "sampler" : Level1_Kaitenzushi_Sampler,
        "max_samples" : 10,
        "level" : "Level 1",
        "name" : "Kaitenzushi",
        "MAX_N" : 500_000,
        "MAX_D" : 1_000_000
    },
    "Rotary Lock 1" : {
        "default_samples" :
            [
                ((3,3,[1,2,3]), 2),
                ((10,4,[9,4,4,8]), 11)
            ],
        "sampler" : Level1_Rotary_Lock_1_Sampler,
        "max_samples" : 10,
        "level" : "Level 1",
        "name" : "Rotary Lock 1",
        "MAX_N" : 50_000_000,
        "MAX_M" : 1_000
    },
    "Scoreboard Inference 1" : {
        "default_samples" :
            [
                ((6,[1,2,3,4,5,6]), 4),
                ((4,[4,3,3,4]), 3),
                ((4,[2,4,6,8]), 4)
            ],
        "sampler" : Level1_Scoreboard_Inference_1_Sampler,
        "max_samples" : 10,
        "level" : "Level 1",
        "name" : "Scoreboard Inference 1",
        "MAX_N" : 500_000,
        "MAX_S" : 1_000_000_000
    },
    "Stack Stabilization 1" : {
        "default_samples" :
            [
                ((5,[2,5,3,6,5]), 3),
                ((3,[100,100,100]), 2),
                ((4,[6,5,4,3]), -1)
            ],
        "sampler" : Level1_Stack_Stabilization_1_Sampler,
        "max_samples" : 10,
        "level" : "Level 1",
        "name" : "Stack Stabilization 1",
        "MAX_N" : 50,
        "MAX_R" : 1_000_000_000
    },
    "Uniform Integers" : {
        "default_samples" :
            [
                ((75, 300), 5),
                ((1, 9), 9),
                ((999999999999, 999999999999), 1)
            ],
        "sampler" : Level1_Uniform_Integers_Sampler,
        "max_samples" : 10,
        "level" : "Level 1",
        "name" : "Uniform Integers",
        "MAX" : 10**12,
    },
}

LEVEL2: Dict[str, Any] = {
    "Director Of Photography" : {
        "default_samples" :
            [
                ((5,'APABA', 1, 2), 1),
                ((5, 'APABA', 2, 3), 0),
                ((8, '.PBAAP.B', 1, 3), 3)
            ],
        "sampler" : Level2_Director_Of_Photography_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Director Of Photography",
        "MAX_N" : 300_000,
        "VALUES" : 'PAB.'
    },
    "Hops" : {
        "default_samples" :
            [
                ((3,1,[1]), 2),
                ((6,3,[5,2,4]), 4)
            ],
        "sampler" : Level2_Hops_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Hops",
        "MAX_N" : 10**12,
        "MAX_F" : 500_000
    },
    "Missing Mail" : {
        "default_samples" :
            [
                ((5,[10,2,8,6,4],5,0.0),25),
                ((5,[10,2,8,6,4],5,1.0),9),
                ((5,[10,2,8,6,4],3,0.5),17),
                ((5,[10,2,8,6,4],3,0.15),20.10825000)
            ],
        "sampler" : Level2_Missing_Mail_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Missing Mail",
        "float_authorized_error" : 10**-6,
        "MAX_N" : 4000,
        "MAX_V" : 1000,
        "MAX_C" : 1000,
        'float_authorized_error' : 10**-6
    },
    "Portals" : {
        "default_samples" :
            [
                ((3,3,[['.', 'E', '.'],['.', '#', 'E'], ['.', 'S', '#']]), 4),
                ((3,4,[['a', '.', 'S', 'a'],['#', '#', '#', '#'], ['E', 'b', '.', 'b']]), -1),
                ((3,4,[['a', 'S', '.', 'b'],['#', '#', '#', '#'], ['E', 'b', '.', 'a']]), 4),
                ((1,9,[['x', 'S', '.', '.', 'x', '.', '.', 'E', 'x']]), 3),
            ],
        "sampler" : Level2_Portals_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Portals",
        "MAX_R" : 50,
        "MAX_C" : 50,
        "VALUES" : '.SE#azertyuiopqsdfghjklmwxcvbn'
    },
    "Rabbit Hole 1" : {
        "default_samples" :
            [
                ((4,[4,1,2,1]), 4),
                ((5,[4,3,5,1,2]),3),
                ((5,[2,4,2,2,3]),4)
            ],
        "sampler" : Level2_Rabbit_Hole_1_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Rabbit Hole 1",
        "MAX_N" : 500_000
    },
    "Rotary Lock 2" : {
        "default_samples" :
            [
                ((3,3,[1,2,3]), 2),
                ((10,4,[9,4,4,8]), 6)
            ],
        "sampler" : Level2_Rotary_Lock_2_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Rotary Lock 2",
        "MAX_N" : 1_000_000_000,
        "MAX_M" : 3_000
    },
    "Scoreboard Inference 2" : {
        "default_samples" :
            [
                ((5, [1,2,3,4,5]), 3),
                ((4, [4,3,3,4]), 2),
                ((4, [2,4,6,8]), 4),
                ((1,[8]), 3)
            ],
        "sampler" : Level2_Scoreboard_Inference_2_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Scoreboard Inference 2",
        "MAX_N" : 500_000,
        "MAX_S" : 1_000_000_000
    },
    "Tunnel Time" : {
        "default_samples" :
            [
                ((10, 2, [1,6], [3, 7], 7), 22),
                ((50, 3, [39, 19, 28], [49, 27, 35], 15), 35)
            ],
        "sampler" : Level2_Tunnel_Time_Sampler,
        "max_samples" : 10,
        "level" : "Level 2",
        "name" : "Tunnel Time",
        "MAX_C" : 10**12,
        "MAX_N" : 500_000,
        "MAX_K" : 10**12
    }
}

LEVEL3: Dict[str, Any] = {
    "Boss Fight" : {
        "default_samples" :
            [
                ((3, [2,1,4], [3,1,2], 4), 6.5),
                ((4,[1, 1, 2, 100],[1, 2, 1, 3],8), 62.75),
                ((4,[1, 1, 2, 3],[1, 2, 1, 100],8), 62.75)
            ],
        "sampler" : Level3_Boss_Fight_Sampler,
        "max_samples" : 10,
        "level" : "Level 3",
        "name" : "Boss Fight",
        "MAX_N" : 500_000,
        "MAX_H" : 1_000_000_000,
        "MAX_D" : 1_000_000_000,
        "MAX_B" : 1_000_000_000,
        'float_authorized_error' : 10**-6
    },
    "Rabbit Hole 2" : {
        "default_samples" :
            [
                ((4, 4, [1,2,3,4], [4,1,2,1]), 4),
                ((5, 6, [3,5,3,1,3,2], [2,1,2,4,5,4]), 4),
                ((10, 9, [3,2,5,9,10,3,3,9,4], [9,5,7,8,6,4,5,3,9]), 5)
            ],
        "sampler" : Level3_Rabbit_Hole_2_Sampler,
        "max_samples" : 10,
        "level" : "Level 3",
        "name" : "Rabbit Hole 2",
        "MAX_N" : 500_000,
        "MAX_M" : 500_000
    },
    "Slippery Trip" : {
        "default_samples" :
            [
                ((3,4,[['.','*','*','*'],['*','*','v','>'],['.','*','.','.']]), 4),
                ((3,3,[['>','*','*'],['*','>','*'],['*','*','>']]), 4),
                ((2,2,[['>','>'],['*','*']]), 0),
                ((4,6,[['>','*','v','*','>','*'],['*','v','*','v','>','*'],['.','*','>','.','.','*'],['.','*','.','.','*','v']]), 6)
            ],
        "sampler" : Level3_Slippery_Trip_Sampler,
        "max_samples" : 10,
        "level" : "Level 3",
        "name" : "Slippery Trip",
        "MAX_R" : 400_000,
        "MAX_C" : 400_000,
        "MAX_RC" : 800_000,
        "VALUES" : '.*v>'
    },
    "Stack Stabilization 2" : {
        "default_samples" :
            [
                ((5,[2,5,3,6,5], 1, 1), 5),
                ((3,[100,100,100], 2, 3), 5),
                ((3, [100,100,100], 7, 3), 9),
                ((4, [6,5,4,3], 10, 1), 19),
                ((4, [100, 100, 1, 1], 2, 1), 207)
            ],
        "sampler" : Level3_Stack_Stabilization_2_Sampler,
        "max_samples" : 10,
        "level" : "Level 3",
        "name" : "Stack Stabilization 2",
        "MAX_N" : 50,
        "MAX_R" : 1_000_000_000,
        "MAX_AB" : 100
    }
}

LEVEL4: Dict[str, Any] = {
    "Conveyor Chaos" : {
        "default_samples" :
            [
                ((2, [10, 20], [100000, 400000], [600000, 800000]), 155000),
                ((5, [2,8,5,9,4], [5000, 2000, 7000, 9000, 0], [7000, 8000, 11000, 11000, 4000]), 36.5)
            ],
        "sampler" : Level4_Conveyor_Chaos_Sampler,
        "max_samples" : 10,
        "level" : "Level 4",
        "name" : "Conveyor Chaos",
        "MAX_N" : 500_000,
        "MAX_H" : 999_999_999,
        "MAX_AB" : 1_000_000,
        'float_authorized_error' : 10**-6
        },
    "Mathematical Art" : {
        "default_samples" :
            [
                ((9, [6, 3, 4, 5, 1, 6, 3, 3, 4], 'ULDRULURD'), 4),
                ((8, [1, 1, 1, 1, 1, 1, 1, 1], "RDLUULDR"), 1),
                ((8, [1, 2, 2, 1, 1, 2, 2, 1], "UDUDLRLR"), 1),
            ],
        "sampler" : Level4_Mathematical_Art_Sampler,
        "max_samples" : 10,
        "level" : "Level 4",
        "name" : "Mathematical Art",
        "MAX_N" : 2_000_000,
        "MAX_L" : 1_000_000_000,
        "DS" : 'UDLR'
    }
}

Warmup_ABCs_generator = ProblemGenerator(**WARMUPS["ABCs"])
Warmup_AllWrong_generator = ProblemGenerator(**WARMUPS["All Wrong"])
Warmup_Battleship_generator = ProblemGenerator(**WARMUPS["Battleship"])

Level1_Cafetaria_generator = ProblemGenerator(**LEVEL1["Cafetaria"])
Level1_DirectorOfPhotography_generator = ProblemGenerator(**LEVEL1["Director Of Photography"])
Level1_Kaitenzushi_generator = ProblemGenerator(**LEVEL1["Kaitenzushi"])
Level1_Rotary_Lock_1_generator = ProblemGenerator(**LEVEL1["Rotary Lock 1"])
Level1_Scoreboard_Inference_1_generator = ProblemGenerator(**LEVEL1["Scoreboard Inference 1"])
Level1_Stack_Stabilization_1_generator = ProblemGenerator(**LEVEL1["Stack Stabilization 1"])
Level1_Uniform_Integers_generator = ProblemGenerator(**LEVEL1["Uniform Integers"])

Level2_DirectorOfPhotography_generator = ProblemGenerator(**LEVEL2["Director Of Photography"])
Level2_Hops_generator = ProblemGenerator(**LEVEL2["Hops"])
Level2_Missing_Mail_generator = ProblemGenerator(**LEVEL2["Missing Mail"])
Level2_Portals_generator = ProblemGenerator(**LEVEL2["Portals"])
Level2_Rabbit_Hole_1_generator = ProblemGenerator(**LEVEL2["Rabbit Hole 1"])
Level2_Rotary_Lock_2_generator = ProblemGenerator(**LEVEL2["Rotary Lock 2"])
Level2_Scoreboard_Inference_2_generator = ProblemGenerator(**LEVEL2["Scoreboard Inference 2"])
Level2_Tunnel_Time_generator = ProblemGenerator(**LEVEL2["Tunnel Time"])

Level3_Boss_Fight_generator = ProblemGenerator(**LEVEL3["Boss Fight"])
Level3_Rabbit_Hole_2_generator = ProblemGenerator(**LEVEL3["Rabbit Hole 2"])
Level3_Slippery_Trip_generator = ProblemGenerator(**LEVEL3["Slippery Trip"])
Level3_Stack_Stabilization_2_generator = ProblemGenerator(**LEVEL3["Stack Stabilization 2"])

Level4_Conveyor_Chaos_generator = ProblemGenerator(**LEVEL4["Conveyor Chaos"])
Level4_Mathematical_Art_generator = ProblemGenerator(**LEVEL4["Mathematical Art"])
