from abc import ABCMeta
from abc import abstractmethod


class AbstractJanitor():
    """
    Abstract base class to be used for custom tear down classes that can be
    added to context then called from after_scenario()
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def clean_up(self):
        pass
