import logging
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


class FieldConnector(BaseConnector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def list_fields() -> list:
        return [
            {
                "name": "custom field1",
                "field": "field-01",
                "text": "text",
                "state": "UP",
                "badge": "badge",
                "list": ["item1", "item2"],
                "dict": {"key1": "value1", "key2": "value2"},
                "datetime": "2023-11-11T00:00.00Z",
                "image": "image",
                "enum": "RUNNING",
                "size": 100,
                "progress": 10,
                "display": {"button": "show"},
                "more": {"code": "HELLO\nPYTHON"},
            },
            {
                "name": "custom field2",
                "field": "field-02",
                "text": "text",
                "state": "UP",
                "badge": "custom badge",
                "list": ["item3", "item4"],
                "dict": {"key3": "value3", "key4": "value4"},
                "datetime": "2023-11-12T00:00.00Z",
                "image": "image",
                "enum": "STOPPED",
                "size": 100,
                "progress": 100,
                "display": {"button": "show"},
                "more": {
                    "code": "import pandas as pd\nimport numpy as np\n\ndf=pd.DataFrame(np.random.randn(10,5))\nprint(df)"
                },
            },
            {
                "name": "custom field3",
                "field": "field-03",
                "text": "text",
                "state": "DOWN",
                "badge": "custom badge",
                "list": ["item5", "item6"],
                "dict": {"key5": "value6", "key7": "value8", "key9": "value10"},
                "datetime": "2023-11-13T00:00.00Z",
                "image": "image",
                "enum": "RUNNING",
                "size": 100,
                "progress": 100,
                "display": {"button": "show"},
                "more": {
                    "code": "spacectl exec init inventory.Collector -j'{\"options\":{}}'"
                },
            },
        ]
