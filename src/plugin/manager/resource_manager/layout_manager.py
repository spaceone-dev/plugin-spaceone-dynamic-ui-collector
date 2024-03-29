import logging
from spaceone.inventory.plugin.collector.lib import *
from plugin.connector.layout_connector import LayoutConnector
from plugin.manager.resource_manager.base import ResourceManager

_LOGGER = logging.getLogger("spaceone")


class LayoutManager(ResourceManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cloud_service_group = "DynamicUI"
        self.cloud_service_type = "Layout"
        self.provider = "spaceone"
        self.metadata_path = "metadata/dynamic_ui/layout.yaml"

    def collect_resources(self, options, secret_data, schema):
        _LOGGER.debug(
            f"[collect_resources] collect Layout resources (options: {options})"
        )
        try:
            yield from self.collect_cloud_service_type(options, secret_data, schema)
            yield from self.collect_cloud_service(options, secret_data, schema)
        except Exception as e:
            yield make_error_response(
                error=e,
                provider=self.provider,
                cloud_service_group=self.cloud_service_group,
                cloud_service_type=self.cloud_service_type,
            )

    def collect_cloud_service_type(self, options, secret_data, schema):
        cloud_service_type = make_cloud_service_type(
            name=self.cloud_service_type,
            group=self.cloud_service_group,
            provider=self.provider,
            metadata_path=self.metadata_path,
            is_primary=True,
            is_major=True,
        )

        yield make_response(
            cloud_service_type=cloud_service_type,
            match_keys=[
                ["name", "reference.resource_id", "account", "provider", "group"]
            ],
            resource_type="inventory.CloudServiceType",
        )

    def collect_cloud_service(self, options, secret_data, schema):
        layout_connector = LayoutConnector()
        layout_items = layout_connector.list_data()
        for layout in layout_items:
            layout = self.set_data_and_yaml(layout, "layouts")
            cloud_service = make_cloud_service(
                name=layout["name"],
                cloud_service_type=self.cloud_service_type,
                cloud_service_group=self.cloud_service_group,
                provider=self.provider,
                data=layout,
            )
            yield make_response(
                cloud_service=cloud_service,
                match_keys=[
                    [
                        "name",
                        "reference.resource_id",
                        "account",
                        "provider",
                        "cloud_service_type",
                    ]
                ],
            )
