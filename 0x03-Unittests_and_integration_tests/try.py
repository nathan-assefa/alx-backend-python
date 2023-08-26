from utils import memoize

class Try:
    def __init__(self, a=5, b=5):
        self.a = a;
        self.b = b;

    def add(self, x, y):
        return x + y
