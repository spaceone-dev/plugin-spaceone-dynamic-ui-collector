import logging
from abc import abstractmethod, ABC
from spaceone.core.manager import BaseManager

_LOGGER = logging.getLogger("spaceone")

__all__ = ["ResourceManager"]


class ResourceManager(BaseManager, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def collect_resources(self, **kwargs):
        pass

    @classmethod
    def list_managers(cls):
        return cls.__subclasses__()
