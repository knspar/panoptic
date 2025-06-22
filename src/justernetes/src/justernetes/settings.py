from typing import Protocol, cast
from dynaconf import Dynaconf, Validator


JUSTNIFFER_CRD_NAME = 'justniffers.knspar.github.io'
JUSTNIFFER_CRD_GROUP = 'knspar.github.io'
JUSTNIFFER_CRD_VERSION = 'v1'
JUSTNIFFER_CRD_PLURAL = 'justniffers'


class Settings(Protocol):
    ENVVAR_PREFIX_FOR_DYNACONF: str
    justniffer_proxy_endpoint: str
    justniffer_proxy_api_key: str
    justniffer_crd_name: str
    justniffer_crd_group: str
    justniffer_crd_version: str
    justniffer_crd_plural: str


    check_interval: int
    def to_dict(self) -> dict: ...


settings: Settings = cast(Settings, Dynaconf(envvar_prefix='JUSTERNETES', 
                              validators=[
                                  Validator('justniffer_proxy_endpoint', required=True),
                                  Validator('justniffer_proxy_api_key', required=True),
                                  Validator('justniffer_crd_name', default=JUSTNIFFER_CRD_NAME),
                                  Validator('justniffer_crd_group', default=JUSTNIFFER_CRD_GROUP),
                                  Validator('justniffer_crd_version', default=JUSTNIFFER_CRD_VERSION),
                                  Validator('justniffer_crd_plural', default=JUSTNIFFER_CRD_PLURAL),
                                  Validator('check_interval', default=60, cast=int)
                              ]))


