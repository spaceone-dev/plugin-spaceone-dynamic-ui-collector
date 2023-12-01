import logging
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


class LayoutConnector(BaseConnector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def list_data() -> list:
        return [
            {
                "name": "custom field1",
                "field": "field-01",
                "text": {
                    "text1": "Dynamic UI 1",
                    "text2": "Dynamic UI 2",
                    "text3": "Dynamic UI 3",
                },
                "enum": {
                    "enum1": "RUNNING",
                    "enum2": "STOPPED",
                    "enum3": "PAUSED",
                },
                "dict": {"key1": "value1", "key2": "value2"},
                "size": {"size1": 100, "size2": 50},
                "datetime": {
                    "datetime1": "2023-11-11T02:53:59.000000+0000",
                    "datetime2": "2023-11-11T11:53:59.000000+0000",
                    "datetime3": "1620034252",
                },
                "state": {
                    "state1": "ACTIVE",
                    "state2": "INACTIVE",
                    "state3": "PAUSED",
                    "state4": "ACTIVE",
                },
                "badge": {
                    "badge1": "RUNNING",
                    "badge2": "STOPPED",
                    "badge3": "PAUSED",
                    "badge4": "RUNNING",
                    "badge5": "RUNNING",
                    "badge6": "RUNNING",
                },
                "more": {
                    "more1": {"button": "show code", "code": "HELLO\nPYTHON"},
                    "more2": {
                        "button": "show table",
                        "data": [
                            {
                                "name": "CUSTOM FIELD1",
                                "type": "general field",
                                "state": "RUNNING",
                            },
                            {
                                "name": "CUSTOM FIELD2",
                                "type": "custom field",
                                "state": "STOPPED",
                            },
                        ],
                    },
                    "more3": {
                        "button": "show items",
                        "data": [
                            {
                                "key": "CUSTOM FIELD1",
                                "value": "general field",
                                "type": "RUNNING",
                            },
                            {
                                "key": "CUSTOM FIELD2",
                                "value": "custom field",
                                "type": "STOPPED",
                            },
                        ],
                    },
                },
            }
        ]
