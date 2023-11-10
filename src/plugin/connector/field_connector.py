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
                'field': 'field-01',
                'text': 'text',
                'state': 'state',
                'badge': 'badge',
                'list': ['item1', 'item2'],
                'dict': {
                    'key1': 'value1',
                    'key2': 'value2'
                },
                'datetime': '2021-01-01T00:00:00Z',
                'image': 'image',
                'enum': 'enum',
                'size': 100,
                'progress': 50
            }
        ]
