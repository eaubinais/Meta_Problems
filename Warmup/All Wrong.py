import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Warmup_AllWrong_generator

wrong = {"A":"B", "B":"A"}

def getWrongAnswers(N: int, C: str) -> str:
    return ''.join(wrong[C[j]] for j in range(N))

if __name__ == "__main__":
    Warmup_AllWrong_generator.evaluate(getWrongAnswers, True)
