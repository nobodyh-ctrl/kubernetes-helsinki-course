# Todo application

Application for **exercise 1.2**. It starts a web server and logs the port it is listening on:

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

## Notes

- The server listens on `0.0.0.0` so it is reachable from inside the cluster.
- No Service or Ingress is created in this exercise.
