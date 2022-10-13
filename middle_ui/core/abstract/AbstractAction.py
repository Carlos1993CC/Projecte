
from abc import ABC, abstractmethod
from typing import Dict

class AbsractAction(ABC):
    def __init__(self, action: str, args: Dict = {}) -> None:
        self.action = action
        self.args = args

    @abstractmethod
    def execute(self):
        pass

    def fail(self):
        pass

    def getID(self):
        return str(self.action)

    def getDevice(self):
        return str(self.device)