from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()

pending_pods = v1.list_pod_for_all_namespaces(field_selector='status.phase=Pending')
for i in pending_pods.items:
    pod_name = i.metadata.name
    try:
        scheduled_node = i.spec.affinity.node_affinity.required_during_scheduling_ignored_during_execution.node_selector_terms[0].match_fields[0].values[0]
        print(f'{pod_name} pending on node {scheduled_node}')
    except:
        print(f'{pod_name} pending')
