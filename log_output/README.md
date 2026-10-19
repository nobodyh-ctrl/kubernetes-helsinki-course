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

Exercise 1.1 uses imperative commands. Declarative YAML is introduced in exercise 1.3.

```bash
kubectl create deployment log-output --image=log-output:dev
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
