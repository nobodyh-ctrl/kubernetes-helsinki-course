# Log output

Application for **exercise 1.1** of the DevOps with Kubernetes course.

It generates a random string at startup, keeps it in memory, and prints it every 5 seconds with a timestamp:

```
2026-10-19T23:33:34+00:00 DSzL01rWOJhR
2026-10-19T23:33:39+00:00 DSzL01rWOJhR
2026-10-19T23:33:44+00:00 DSzL01rWOJhR
```

The string stays the same while the process is alive. When the pod is recreated, a new string is generated.

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
