import kubernetes.client
import kubernetes.config
from kubernetes.client.rest import ApiException
from dataclasses import dataclass
from enum import StrEnum, auto
from justserver.logging import logger
# Define an Enum for Kubernetes object types


class KType(StrEnum):
    pod = auto()
    service_cluster_ip = auto()
    service_external_ip = auto()
    node_internal_ip = auto()
    node_external_ip = auto()

# Define a dataclass to hold resolved Kubernetes object information


@dataclass
class Resolved:
    name: str
    type: KType


def get_kubernetes_ips() -> dict[str, Resolved]:

    kubernetes.config.load_config()

    v1 = kubernetes.client.CoreV1Api()

    resolved_ips: dict[str, Resolved] = {}

    logger.debug("\n--- Collecting Pod IPs ---")
    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        if pod.status and pod.status.pod_ip and pod.metadata and pod.metadata.name:
            resolved_ips[pod.status.pod_ip] = Resolved(name=pod.metadata.name, type=KType.pod)
    logger.debug(f"Found {len([r for r in resolved_ips.values() if r.type == KType.pod])} Pod IPs.")

    logger.debug("\n--- Collecting Service IPs ---")
    services = v1.list_service_for_all_namespaces(watch=False)
    for svc in services.items:
        # Get ClusterIP
        if svc.spec and svc.spec.cluster_ip and svc.spec.cluster_ip != "None" and svc.metadata and svc.metadata.name:
            resolved_ips[svc.spec.cluster_ip] = Resolved(name=svc.metadata.name, type=KType.service_cluster_ip)

        # Get External IPs for LoadBalancer services
        if svc.status and svc.status.load_balancer and svc.status.load_balancer.ingress and svc.metadata and svc.metadata.name:
            for ingress in svc.status.load_balancer.ingress:
                if ingress.ip:
                    resolved_ips[ingress.ip] = Resolved(name=svc.metadata.name, type=KType.service_external_ip)
    logger.debug(f"Found {len([r for r in resolved_ips.values() if r.type in [KType.service_cluster_ip, KType.service_external_ip]])} Service IPs.")

    logger.debug("\n--- Collecting Node IPs ---")
    nodes = v1.list_node(watch=False)
    for node in nodes.items:
        if node.status and node.status.addresses and node.metadata and node.metadata.name:
            for address in node.status.addresses:
                if address.type == "InternalIP":
                    resolved_ips[address.address] = Resolved(name=node.metadata.name, type=KType.node_internal_ip)
                elif address.type == "ExternalIP":
                    resolved_ips[address.address] = Resolved(name=node.metadata.name, type=KType.node_external_ip)
    logger.debug(f"Found {len([r for r in resolved_ips.values() if r.type in [KType.node_internal_ip, KType.node_external_ip]])} Node IPs.")

    return resolved_ips


# Example Usage:
if __name__ == "__main__":
    # Call the function to get IP addresses and resolved objects
    resolved_ips = get_kubernetes_ips()

    # Print the collected IP addresses and their resolved information
    if resolved_ips:
        logger.debug("\n--- Collected IP Addresses Summary ---")
        # Sort by IP address for consistent output
        for ip, resolved_obj in sorted(resolved_ips.items()):
            logger.debug(f"  - '{resolved_obj.name}': '{ip}' (Type: '{resolved_obj.type.value}')")  # Using .value to get string from Enum
    else:
        logger.debug("\nCould not collect IP addresses. Please check the error messages above.")
