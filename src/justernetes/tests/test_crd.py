from justernetes.logging import logger
from justernetes.crd import JustnifferCRD


def test1():
    body = {'apiVersion': 'knspar.github.io/v1', 'kind': 'Justniffer',
            'metadata': {'creationTimestamp': '2025-06-04T20:31:34Z',
                          'finalizers': ['kopf.zalando.org/KopfFinalizerMarker'],
                          'generation': 1,
                         'managedFields': [{'apiVersion': 'knspar.github.io/v1', 'fieldsType': 'FieldsV1', 'fieldsV1': {'f:spec': {'.': {}, 'f:encode': {}, 'f:filter': {}, 'f:in_the_middle': {}, 'f:interface': {}, 'f:newline': {}, 'f:truncated': {}}}, 'manager': 'dashboard-api', 'operation': 'Update', 'time': '2025-06-04T20:31:34Z'}, {
                             'apiVersion': 'knspar.github.io/v1', 'fieldsType': 'FieldsV1', 'fieldsV1': {'f:metadata': {'f:finalizers': {'.': {}, 'v:"kopf.zalando.org/KopfFinalizerMarker"': {}}}}, 'manager': 'kopf', 'operation': 'Update', 'time': '2025-06-04T20:31:35Z'}], 'name': 'my-web-sniffer1', 'namespace': 'justserver', 'resourceVersion': '10386322', 'uid': 'a84079b4-7f80-48f9-8b6f-55a95cba49b8'}, 'spec': {'encode': 'hex_encode', 'filter': 'tcp port 80 or tcp port 443', 'in_the_middle': True, 'interface': 'eth0', 'newline': False, 'truncated': False}}
    logger.info(f'Created Justniffer {body["metadata"]["name"]}')
    obj =JustnifferCRD.model_validate(
        body
    )
    logger.info(f'Created Justniffer {obj.metadata.name} {obj=}')
