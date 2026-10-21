# Log output

Application for **exercises 1.1, 1.3, 1.7 and 1.9** of the DevOps with Kubernetes course.

It generates a random string at startup, keeps it in memory, and prints it every 5 seconds with a timestamp:

```
2026-10-19T23:33:34+00:00 DSzL01rWOJhR
2026-10-19T23:33:39+00:00 DSzL01rWOJhR
2026-10-19T23:33:44+00:00 DSzL01rWOJhR
```

The string stays the same while the process is alive. When the pod is recreated, a new string is generated.

Since exercise 1.7 the application also serves the current status over HTTP at `/` and `/status`:

## Build the image

```bash
docker build -t log-output:dev .
```

## Import the image into the cluster

The image is built locally, so the cluster cannot pull it from a registry. With k3d, import it directly into the nodes:

```bash
k3d image import log-output:dev -c k3s-default
```

Because the tag is not `latest`, Kubernetes uses `imagePullPolicy: IfNotPresent` by default and uses the imported image.

## Deploy

### Imperative (exercise 1.1)

```bash
kubectl create deployment log-output --image=log-output:dev
```

### Declarative (exercise 1.3)

The same deployment is defined in `manifests/deployment.yaml`, so it can be applied from the file instead:

```bash
kubectl apply -f manifests/deployment.yaml
```

Check that the pod is running:

```bash
kubectl get pods
kubectl rollout status deployment/log-output
```

## Status endpoint and Ingress (exercises 1.7 and 1.9)

The Service and Ingress are defined in `manifests/`:

```bash
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

In this k3d cluster, the load balancer publishes port 80 on host port `8081`, so the page is available at <http://localhost:8081>:

```
Timestamp: 2026-10-21T00:11:47+00:00
Random string: cxLEPeniuKAn
```

Since exercise 1.9 the same Ingress also routes `/pingpong` to the `ping-pong` Service, so both applications share access:

- `/pingpong` → `ping-pong:2345`
- `/` → `log-output:2345`

> The Ingress uses `/` without a host, so only one such Ingress can be active. The todo-app Ingress also uses `/`; delete `dwk-material-ingress` while working on exercise 1.9 (see `ping-pong/README.md`).

## Read the logs

```bash
kubectl logs -f deployment/log-output
```

## Useful commands

```bash
# Restart the pod: the random string changes because the process starts again
kubectl rollout restart deployment/log-output

# Watch the new pod
kubectl logs -f deployment/log-output

# Remove the deployment
kubectl delete deployment log-output
```
