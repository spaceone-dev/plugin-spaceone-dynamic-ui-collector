import logging

from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer
from plugin.manager.resource_manager import ResourceManager

_LOGGER = logging.getLogger("cloudforet")

app = CollectorPluginServer()


@app.route("Collector.init")
def collector_init(params: dict) -> dict:
    return {"metadata": {"options_schema": _create_options_schema()}}


@app.route("Collector.verify")
def collector_verify(params: dict) -> dict:
    pass


@app.route("Collector.collect")
def collector_collect(params: dict) -> dict:
    options = params["options"]
    secret_data = params["secret_data"]
    schema = params.get("schema")

    resource_mgrs = ResourceManager.list_managers()
    for manager in resource_mgrs:
        results = manager().collect_resources(options, secret_data, schema)

        for result in results:
            yield result


@app.route("Job.get_tasks")
def job_get_tasks(params: dict) -> dict:
    pass


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
