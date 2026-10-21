# Ping-pong

Application for **exercise 1.9** of the DevOps with Kubernetes course.

It responds to `GET /pingpong` with `pong <counter>` and increments an in-memory counter:

```
pong 0
pong 1
pong 2
```

The counter starts at `0` and is reset when the pod restarts. With more than one replica, each pod keeps its own counter.

The application uses Flask; its dependency is declared in `requirements.txt` and installed by the Dockerfile.

## Build the image

```bash
docker build -t ping-pong:dev .
```

## Import the image into the cluster

```bash
k3d image import ping-pong:dev -c k3s-default
```

## Deploy

```bash
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
```

Check that the pod is running:

```bash
kubectl get pods
kubectl rollout status deployment/ping-pong
```

## Share access with the log output application

The shared Ingress is `log_output/manifests/ingress.yaml` and routes:

- `/pingpong` → `ping-pong:2345`
- `/` → `log-output:2345`

Because the todo-app Ingress also uses `/` without a host, remove it while working on this exercise:

```bash
kubectl delete ingress dwk-material-ingress --ignore-not-found
kubectl apply -f ../log_output/manifests/ingress.yaml
```

Then, from the host:

```bash
curl http://localhost:8081/pingpong   # pong 0
curl http://localhost:8081/pingpong   # pong 1
curl http://localhost:8081/           # log output page
```

## Access without the Ingress

For a quick check, forward the Service port:

```bash
kubectl port-forward svc/ping-pong 8080:2345
curl http://localhost:8080/pingpong
```
