from abc import ABC, abstractmethod
import sys

class Model(ABC):
    def __init__(self, delay):
        self.delay = delay

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def update(self):
        pass

sys.modules[__name__] = Model
