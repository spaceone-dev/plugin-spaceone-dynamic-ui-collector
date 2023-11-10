import logging
from spaceone.core.manager import BaseManager
from spaceone.inventory.plugin.collector.lib import *
from ..connector.field_connector import FieldConnector

_LOGGER = logging.getLogger('cloudforet')


class FieldManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cloud_service_group = 'DynamicUI'
        self.cloud_service_type = 'Field'
        self.provider = 'spaceone_company'
        self.metadata_path = 'plugin/metadata/dynamic_ui/field.yaml'

    def collect_resources(self, options, secret_data, schema):
        try:
            yield from self.collect_cloud_service_type(options, secret_data, schema)
        except Exception as e:
            yield make_error_response(
                error=e,
                provider=self.provider,
                cloud_service_group=self.cloud_service_group,
                cloud_service_type=self.cloud_service_type,
                resource_type='inventory.CloudServiceType',
            )

        try:
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
            metadata_path=self.metadata_path
        )

        yield make_response(
            cloud_service_type=cloud_service_type,
            match_keys=[['name', 'reference.resource_id', 'account', 'provider']],
            resource_type='inventory.CloudServiceType'
        )

    def collect_cloud_service(self, options, secret_data, schema):
        field_connector = FieldConnector()
        field_items = field_connector.list_fields()
        for item in field_items:
            cloud_service = make_cloud_service(
                name=self.cloud_service_type,
                cloud_service_type=self.cloud_service_type,
                cloud_service_group=self.cloud_service_group,
                provider=self.provider,
                data=item
            )
            yield make_response(
                cloud_service=cloud_service,
                match_keys=[['name', 'reference.resource_id', 'account', 'provider']]
            )
