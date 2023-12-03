import os
import logging
from spaceone.core.utils import dump_yaml, load_yaml_from_file
from spaceone.core import config
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

    @staticmethod
    def set_data_and_yaml(field, folder_name):
        project_path = __import__(config.get_package()).__path__[0]
        file_path = os.path.join(
            project_path, "metadata", "dynamic_ui", f"{folder_name}"
        )

        for file in os.listdir(file_path):
            if file.endswith(".yaml") or file.endswith(".yml"):
                field_type, _ = file.rsplit("_", 1)

                field[f"{field_type}_example"] = {
                    "data": {
                        "data": {f"{field_type}": field.get(field_type, {})},
                    },
                    "yaml": dump_yaml(
                        load_yaml_from_file(os.path.join(file_path, file))
                    ),
                }
        return field
