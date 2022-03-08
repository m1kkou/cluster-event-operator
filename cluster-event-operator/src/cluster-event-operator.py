import os
from typing import Counter
import kopf
import kubernetes
from kubernetes.client.rest import ApiException
import yaml

counter = 0

@kopf.on.create('pod')
def create_fn(body, **kwargs):
    global counter
    print(f"A handler is called with body: {body}")

    # Actually create an object by requesting the Kubernetes API.
    api = kubernetes.client.CustomObjectsApi()

    test_resource = {
        "apiVersion": "kopf.dev/v1",
        "kind": "ClusterEvent",
        "metadata": {"name": f"test-cluster-event-from-operator-{counter}"},
        "spec": {"size": "4G"},
    }

    created_resource = api.create_cluster_custom_object(
        group="kopf.dev",
        version="v1",
        plural="clusterevents",
        body=test_resource,
    )

    counter += 1
    
    print("[INFO] Custom resource `test-clusterevent` created!\n")
