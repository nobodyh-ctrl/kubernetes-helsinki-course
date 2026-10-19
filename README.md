# DevOps with Kubernetes — Course Exercises

My solutions for the [DevOps with Kubernetes](https://devopswithkubernetes.com/) course from the University of Helsinki.

Every exercise is developed incrementally and published as its own **GitHub release**, so the repository history doubles as a record of progress.

---

## Repository layout

```
.
├── part-1/          # Introduction to Kubernetes
│   ├── 1.1/
│   ├── 1.2/
│   └── ...
├── part-2/          # Deploying applications
├── part-3/          # Managing deployments
├── part-4/          # Applying Kubernetes
└── part-5/          # Kubernetes in practice
```

Each exercise directory is self-contained: Kubernetes manifests, application source when needed, and a short `README.md` describing what was done and how to run it.

## Releases

Each completed exercise gets:

- One commit containing that exercise's files
- An annotated tag in the form `<part>.<exercise>` (e.g. `1.1`, `2.3`, `4.10`)
- A GitHub release with the tag, using the exercise number as the title

This makes it easy to review a single exercise without digging through later changes:

```bash
git checkout 1.1                    # inspect the repository at that exercise
kubectl apply -f part-1/1.1/ -n <namespace>
```

The `main` branch always contains every exercise completed so far.

## Progress

| Part | Topic | Exercises | Status |
| ---- | ----- | --------- | ------ |
| 1 | Introduction to Kubernetes | 1.1 – 1.13 | 🚧 In progress |
| 2 | Deploying applications | 2.1 – 2.10 | ⏳ Pending |
| 3 | Managing deployments | 3.1 – 3.12 | ⏳ Pending |
| 4 | Applying Kubernetes | 4.1 – 4.10 | ⏳ Pending |
| 5 | Kubernetes in practice | 5.1 – ... | ⏳ Pending |

## Prerequisites

- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- A local cluster: [k3d](https://k3d.io/) or [kind](https://kind.sigs.k8s.io/)
- [Docker](https://docs.docker.com/get-docker/)
- [Helm](https://helm.sh/) (from part 2 onwards)

## Notes

- Exercises follow the course order; solutions are my own unless stated otherwise.
- Manifests target a local k3d cluster unless an exercise requires a cloud provider.
- Older exercises may not be updated to the latest API versions — they reflect the state of the course at the time.
