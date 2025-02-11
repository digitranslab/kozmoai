---
title: Kubernetes
slug: /deployment-kubernetes
---



This guide will help you get KozmoAi up and running in Kubernetes cluster, including the following steps:

- Install [KozmoAi as IDE](/deployment-kubernetes) in a Kubernetes cluster (for development)
- Install [KozmoAi as a standalone application](/deployment-kubernetes) in a Kubernetes cluster (for production runtime workloads)

## KozmoAi (IDE) {#cb60b2f34e70490faf231cb0fe1a4b42}


---


This solution is designed to provide a complete environment for developers to create, test, and debug their flows. It includes both the API and the UI.


### Prerequisites {#3efd3c63ff8849228c136f9252e504fd}

- Kubernetes server
- kubectl
- Helm

### Step 0. Prepare a Kubernetes cluster {#290b9624770a4c1ba2c889d384b7ef4c}


We use [Minikube](https://minikube.sigs.k8s.io/docs/start/) for this example, but you can use any Kubernetes cluster.

1. Create a Kubernetes cluster on Minikube.

	```text
	minikube start
	```

2. Set `kubectl` to use Minikube.

	```text
	kubectl config use-context minikube
	```


### Step 1. Install the KozmoAi Helm chart {#b5c2a35144634a05a392f7e650929efe}

1. Add the repository to Helm.

	```text
	helm repo add kozmoai <https://digitranslab.github.io/kozmoai-helm-charts>
	helm repo update
	```

2. Install KozmoAi with the default options in the `kozmoai` namespace.

	```text
	helm install kozmoai-ide digitranslab/kozmoai-ide -n kozmoai --create-namespace
	```

3. Check the status of the pods

	```text
	kubectl get pods -n kozmoai
	```


	```text
	NAME                                 READY   STATUS    RESTARTS       AGE
	kozmoai-0                           1/1     Running   0              33s
	kozmoai-frontend-5d9c558dbb-g7tc9   1/1     Running   0              38s
	```


### Step 2. Access KozmoAi {#34c71d04351949deb6c8ed7ffe30eafb}


Enable local port forwarding to access KozmoAi from your local machine.


```text
kubectl port-forward -n kozmoai svc/kozmoai-kozmoai-runtime 7860:7860
```


Now you can access KozmoAi at `http://localhost:7860/`.


### KozmoAi version {#645c6ef7984d4da0bcc4170bab0ff415}


To specify a different KozmoAi version, you can set the `kozmoai.backend.image.tag` and `kozmoai.frontend.image.tag` values in the `values.yaml` file.


```yaml
kozmoai:
  backend:
    image:
      tag: "1.0.0a59"
  frontend:
    image:
      tag: "1.0.0a59"

```


### Storage {#6772c00af79147d293c821b4c6905d3b}


By default, the chart will use a SQLLite database stored in a local persistent disk.
If you want to use an external PostgreSQL database, you can set the `kozmoai.database` values in the `values.yaml` file.


```yaml
# Deploy postgresql. You can skip this section if you have an existing postgresql database.
postgresql:
  enabled: true
  fullnameOverride: "kozmoai-ide-postgresql-service"
  auth:
    username: "kozmoai"
    password: "kozmoai-postgres"
    database: "kozmoai-db"

kozmoai:
  backend:
    externalDatabase:
      enabled: true
      driver:
        value: "postgresql"
      host:
        value: "kozmoai-ide-postgresql-service"
      port:
        value: "5432"
      database:
        value: "kozmoai-db"
      user:
        value: "kozmoai"
      password:
        valueFrom:
          secretKeyRef:
            key: "password"
            name: "kozmoai-ide-postgresql-service"
    sqlite:
      enabled: false

```


### Scaling {#e1d95ba6551742aa86958dc03b26129e}


You can scale the number of replicas for the KozmoAi backend and frontend services by changing the `replicaCount` value in the `values.yaml` file.


```yaml
kozmoai:
  backend:
    replicaCount: 3
  frontend:
    replicaCount: 3

```


You can scale frontend and backend services independently.


To scale vertically (increase the resources for the pods), you can set the `resources` values in the `values.yaml` file.


```yaml
kozmoai:
  backend:
    resources:
      requests:
        memory: "2Gi"
        cpu: "1000m"
  frontend:
    resources:
      requests:
        memory: "1Gi"
        cpu: "1000m"

```


### Deploy on AWS EKS, Google GKE, or Azure AKS and other examples {#a8c3d4dc4e4f42f49b21189df5e2b851}


Visit the [KozmoAi Helm Charts repository](https://github.com/digitranslab/kozmoai-helm-charts) for more information.


## KozmoAi (Runtime) {#49f2813ad2d3460081ad26a286a65e73}


---


The runtime chart is tailored for deploying applications in a production environment. It is focused on stability, performance, isolation, and security to ensure that applications run reliably and efficiently.


Using a dedicated deployment for a set of flows is fundamental in production environments to have granular resource control.


### Prerequisites {#3ad3a9389fff483ba8bd309189426a9d}

- Kubernetes server
- kubectl
- Helm

### Step 0. Prepare a Kubernetes cluster {#aaa764703ec44bd5ba64b5ef4599630b}


Follow the same steps as for the KozmoAi IDE.


### Step 1. Install the KozmoAi runtime Helm chart {#72a18aa8349c421186ba01d73a002531}

1. Add the repository to Helm.

	```shell
	helm repo add kozmoai <https://digitranslab.github.io/kozmoai-helm-charts>
	helm repo update
	```

2. Install the KozmoAi app with the default options in the `kozmoai` namespace.
If you bundled the flow in a docker image, you can specify the image name in the `values.yaml` file or with the `-set` flag:
If you want to download the flow from a remote location, you can specify the URL in the `values.yaml` file or with the `-set` flag:

	```shell
	helm install my-kozmoai-app digitranslab/kozmoai-runtime -n kozmoai --create-namespace --set image.repository=myuser/kozmoai-just-chat --set image.tag=1.0.0
	
	```


	```shell
	helm install my-kozmoai-app digitranslab/kozmoai-runtime -n kozmoai --create-namespace --set downloadFlows.flows[0].url=https://raw.githubusercontent.com/digitranslab/kozmoai/dev/src/backend/base/kozmoai/initial_setup/starter_projects/Basic%20Prompting%20(Hello%2C%20world!).json
	
	```

3. Check the status of the pods.

	```text
	kubectl get pods -n kozmoai
	
	```


### Step 2. Access the KozmoAi app API {#e13326fc07734e4aa86dfb75ccfa31f8}


Enable local port forwarding to access KozmoAi from your local machine.


```text
kubectl port-forward -n kozmoai svc/kozmoai-my-kozmoai-app 7860:7860
```


Now you can access the API at `http://localhost:7860/api/v1/flows` and execute the flow:


```shell
id=$(curl -s <http://localhost:7860/api/v1/flows> | jq -r '.flows[0].id')
curl -X POST \\
    "<http://localhost:7860/api/v1/run/$id?stream=false>" \\
    -H 'Content-Type: application/json'\\
    -d '{
      "input_value": "Hello!",
      "output_type": "chat",
      "input_type": "chat"
    }'

```


### Storage {#09514d2b59064d37b685c7c0acecb861}


In this case, storage is not needed as our deployment is stateless.


### Log level and KozmoAi configurations {#ecd97f0be96d4d1cabcc5b77a2d00980}


You can set the log level and other KozmoAi configurations in the `values.yaml` file.


```yaml
env:
  - name: KOZMOAI_LOG_LEVEL
    value: "INFO"

```


### Configure secrets and variables {#b91929e92acf47c183ea4c9ba9d19514}


To inject secrets and KozmoAi global variables, you can use the `secrets` and `env` sections in the `values.yaml` file.


Let's say your flow uses a global variable which is a secret; when you export the flow as JSON, it's recommended to not include it.
When importing the flow in the KozmoAi runtime, you can set the global variable using the `env` section in the `values.yaml` file.
Assuming you have a global variable called `openai_key_var`, you can read it directly from a secret:


```yaml
env:
  - name: openai_key_var
    valueFrom:
      secretKeyRef:
        name: openai-key
        key: openai-key

```


or directly from the values file (not recommended for secret values!):


```yaml
env:
  - name: openai_key_var
    value: "sk-...."

```


### Scaling {#359b9ea5302147ebbed3ab8aa49dae8d}


You can scale the number of replicas for the KozmoAi app by changing the `replicaCount` value in the `values.yaml` file.


```yaml
replicaCount: 3

```


To scale vertically (increase the resources for the pods), you can set the `resources` values in the `values.yaml` file.


```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"

```


## Other Examples {#8522b4276b51448e9f8f0c6efc731a7c}


---


Visit the KozmoAi Helm Charts repository for more examples and configurations. Use the default values file as reference for all the options available.


:::note

Visit the examples directory to learn more about different deployment options.

:::



