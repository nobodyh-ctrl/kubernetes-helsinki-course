# Todo application

Application for the course project. It starts a web server, logs the port it is listening on, and serves a simple HTML page at `/`:

```
Server started in port 8000
```

The port comes from the `PORT` environment variable, falling back to `8000` when it is not set. External access is configured from exercise 1.6 onwards.

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

## Access through the NodePort service (exercise 1.6, superseded)

Exercise 1.6 exposed the application with a `NodePort` Service (`nodePort: 30080`, published on host port `8082`). In exercise 1.8 the Service became `ClusterIP` and access moved to an Ingress.

## Access through Ingress (exercise 1.8)

```bash
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

The Service is now `ClusterIP` on port `2345` (→ `targetPort 8000`) and the Ingress routes `/` to it.

k3d publishes port 80 on host port `8081`, so the application is available at <http://localhost:8081>.

> The log output Ingress was deleted in this exercise because both Ingresses used `/` without a host and would conflict.

## Notes

- The server listens on `0.0.0.0` so it is reachable from inside the cluster.
- The page is rendered from `templates/index.html`.
- The Service selects the pod through the `app: todo-app` label; the Ingress routes to the Service.
