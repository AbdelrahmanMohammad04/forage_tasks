from abc import ABC, abstractclassmethod

class Servicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass