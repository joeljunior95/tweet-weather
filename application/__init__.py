from abc import ABCMeta
from abc import abstractmethod


class BaseApplication(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...
