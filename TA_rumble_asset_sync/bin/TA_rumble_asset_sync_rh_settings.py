
import ta_rumble_asset_sync_declare

from splunktaucclib.rest_handler.endpoint import (
    field,
    validator,
    RestModel,
    MultipleModel,
)

from splunktaucclib.rest_handler import admin_external, util
from splunktaucclib.rest_handler.admin_external import AdminExternalHandler
from splunk_aoblib.rest_migration import ConfigMigrationHandler
from splunktaucclib.rest_handler.endpoint.validator import Validator

util.remove_http_proxy_env_vars()

fields_proxy = [
    field.RestField(
        'proxy_enabled',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'proxy_type',
        required=True,
        encrypted=False,
        default='http',
        validator=None
    ), 
    field.RestField(
        'proxy_rdns',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'proxy_url',
        required=False,
        encrypted=False,
        default=None,
        validator=validator.String(
            max_len=4096, 
            min_len=0, 
        )
    ), 
    field.RestField(
        'proxy_port',
        required=False,
        encrypted=False,
        default=None,
        validator=validator.Number(
            max_val=65535, 
            min_val=1, 
        )
    ), 
    field.RestField(
        'proxy_username',
        required=False,
        encrypted=False,
        default=None,
        validator=validator.String(
            min_len=0, 
            max_len=256, 
        )
    ), 
    field.RestField(
        'proxy_password',
        required=False,
        encrypted=True,
        default=None,
        validator=validator.String(
            min_len=0, 
            max_len=256, 
        )
    )
]
model_proxy = RestModel(fields_proxy, name='proxy')


fields_logging = [
    field.RestField(
        'loglevel',
        required=False,
        encrypted=False,
        default='INFO',
        validator=None
    )
]
model_logging = RestModel(fields_logging, name='logging')

endpoint = MultipleModel(
    'ta_rumble_asset_sync_settings',
    models=[
        model_proxy, 
        model_logging
    ],
)

if __name__ == '__main__':
    admin_external.handle(
        endpoint,
        handler=ConfigMigrationHandler,
    )
