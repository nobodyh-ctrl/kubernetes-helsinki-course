# Kubernetes diagrams

Draw.io diagrams for the cluster state at the end of **exercise 1.9**.

Open any `.drawio` file with the [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) extension in VS Code. The files are plain, uncompressed XML, so they also work with the draw.io desktop app and <https://app.diagrams.net>.

PNG exports generated from the sources are available as `*.drawio.png` and are embedded in the repository's main `README.md`.

| File | What it shows |
| ---- | ------------- |
| `cluster-topology.drawio` | Physical layout: WSL host, k3d serverlb, Docker network, the three K3s node containers, and the pods scheduled on each node. Includes host port mappings and node IPs. |
| `ingress-routing.drawio` | Request flow from `localhost:8081` through Traefik and `log-output-ingress` to the log-output and ping-pong Services and Pods. |
| `workloads-and-services.drawio` | How each Deployment creates a ReplicaSet and Pod, and how the Service selector matches the pod label. |

## Notes

- Only `log-output-ingress` is active in 1.9. The todo-app keeps running but has no Ingress, so it does not compete for `/`.
- IPs, pod names, and ReplicaSet hashes reflect the live cluster when the diagrams were generated. Recreating the cluster changes them.
- The diagrams use basic draw.io shapes, so they can be edited without external icon libraries.
