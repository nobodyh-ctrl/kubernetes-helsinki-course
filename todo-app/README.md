# Todo application

Application for the course project. It starts a web server, logs the port it is listening on, and serves a simple HTML page at `/`:

```
Server started in port 8000
```

The port comes from the `PORT` environment variable, falling back to `8000` when it is not set. There is no external access yet: networking is configured in a later exercise.

## Build the image

```bash
docker build -t todo-app:dev .
```

## Import the image into the cluster

```bash
k3d image import todo-app:dev -c k3s-default
```

## Deploy

### Imperative (exercise 1.2)

```bash
kubectl create deployment todo-app --image=todo-app:dev
kubectl set env deployment/todo-app PORT=8000
```

`kubectl set env` triggers a new rollout, so the container starts with `PORT` set.

### Declarative (exercise 1.4)

The deployment is defined in `manifests/deployment.yaml`:

```bash
kubectl apply -f manifests/deployment.yaml
```

The manifest does not set `PORT`, so the application uses its default (`8000`).

Check the result:

```bash
kubectl get pods
kubectl rollout status deployment/todo-app
kubectl logs deployment/todo-app
```

## Access the application (exercise 1.5)

There is no Service or Ingress yet, so the page is reached through a port-forward:

```bash
kubectl port-forward deployment/todo-app 8000:8000
```

Then open <http://localhost:8000>.

Because the image tag stays `todo-app:dev`, after rebuilding you need to refresh the image in the cluster and restart the pod:

```bash
docker build -t todo-app:dev .
k3d image import todo-app:dev -c k3s-default
kubectl rollout restart deployment/todo-app
```

## Access through the NodePort service (exercise 1.6)

```bash
kubectl apply -f manifests/service.yaml
```

The Service is of type `NodePort`:

- `port: 1234` — port exposed inside the cluster
- `targetPort: 8000` — port the application listens on
- `nodePort: 30080` — port opened on every node

In this k3d cluster, node port `30080` is published on host port `8082`:

```bash
docker port k3d-k3s-default-serverlb
# 30080/tcp -> 0.0.0.0:8082
```

The application is then available at <http://localhost:8082>.

## Notes

- The server listens on `0.0.0.0` so it is reachable from inside the cluster.
- The page is rendered from `templates/index.html`.
- The NodePort Service selects the pod through the `app: todo-app` label.
