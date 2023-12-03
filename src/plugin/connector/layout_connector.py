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
                "item": {"field_id": "field-01", "state": "RUNNING", "size": 100},
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
                "simple_table": [
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
                    {
                        "name": "CUSTOM FIELD3",
                        "type": "custom field",
                        "state": "PAUSED",
                    },
                ],
                "query_search_table": [
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
                    {
                        "name": "CUSTOM FIELD3",
                        "type": "custom field",
                        "state": "PAUSED",
                    },
                ],
                "table": [
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
                    {
                        "name": "CUSTOM FIELD3",
                        "type": "custom field",
                        "state": "PAUSED",
                    },
                ],
                "raw": "import os\nimport sys\n\nprint('hello world')",
                "html": """
        ELB Network Load Balancer 한도의 80%가 넘는 사용량을 검사합니다. 
        Classic Load Balancer와 Application Load Balancer는 별도의 한도를 가지고 있습니다.
        스냅샷을 기반으로 값이 계산되기 때문에 현재 사용량은 다를 수 있습니다. 
        한도 및 사용량 데이터에 변경 사항을 반영하는 데 최대 24시간이 걸릴 수 있습니다. 
        최근에 한도가 상향 조정된 경우에는 사용률이 일시적으로 한도를 초과하는 것을 확인할 수 있습니다.
        <br/>\n
        <br>\n
        <b>알림 기준</b>
        <br>\n노란색: 한도의 80%에 도달했습니다.
        <br>\n빨간색: 한도의 100%에 도달했습니다.
        <br>\n파란색: Trusted Advisor가 한 개 이상의 리전에서 사용률 또는 한도를 가져올 수 없습니다.
        <br>\n
        <br>\n
        <b>권장 조치</b>
        <br>\n서비스 한도가 초과할 것으로 예상될 때는 지원 센터에서 케이스를 생성하여 
        <a href="https://aws.amazon.com/support/createCase?type=service_limit_increase" target=\"_blank\">
        한도 상향 조정을 요청</a>합니다.
        <br>\n
        <br>\n
        <b>추가 리소스</b>
        <br>\n
        <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_elastic_load_balancer" target=\"_blank\">
        AWS 서비스 한도 - Elastic Load Balancing 기본 서비스 한도
        </a>
                """,
                "markdown": """
                # ELB Network Load Balancer 한도의 80%가 넘는 사용량을 검사합니다.
                * Classic Load Balancer와 Application Load Balancer는 별도의 한도를 가지고 있습니다.
                * 스냅샷을 기반으로 값이 계산되기 때문에 현재 사용량은 다를 수 있습니다.
                * 한도 및 사용량 데이터에 변경 사항을 반영하는 데 최대 24시간이 걸릴 수 있습니다.
                """,
            }
        ]
