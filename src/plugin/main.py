import logging

from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer
from plugin.manager.field_manager import FieldManager

_LOGGER = logging.getLogger("cloudforet")

app = CollectorPluginServer()


@app.route("Collector.init")
def collector_init(params: dict) -> dict:
    return {"metadata": {"options_schema": _create_options_schema()}}


@app.route("Collector.collect")
def collector_collect(params: dict) -> dict:
    options = params["options"]
    secret_data = params["secret_data"]
    schema = params.get("schema")

    field_manager = FieldManager()
    return field_manager.collect_resources(options, secret_data, schema)


def _create_options_schema():
    return {
        "required": ["items"],
        "order": ["items"],
        "type": "object",
        "properties": {
            "items": {
                "title": "Item filter",
                "type": "array",
                "items": {"enum": ["fields"]},
            }
        },
    }


@app.route("Job.get_tasks")
def job_get_tasks(params: dict) -> dict:
    """Get job tasks

    Args:
        params (JobGetTaskRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'domain_id': 'str'
        }

    Returns:
        TasksResponse: {
            'tasks': 'list'
        }

    """
    return {"tasks": []}
