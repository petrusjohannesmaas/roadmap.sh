# Blue-Green Deployments with Kubernetes

## 📘 Overview

**Blue-green deployment** is a release strategy that runs two versions of an application (blue and green) simultaneously. It helps minimize downtime and risk by gradually shifting traffic from the old version (blue) to the new one (green). If an issue arises, traffic can quickly revert back to the blue environment.

This project uses **native Kubernetes resources**—**Deployments** and **Services**—to demonstrate a basic blue-green deployment strategy, without relying on GitHub Actions or CI/CD pipelines (yet).

---

## ✅ Prerequisites

To use this repo, make sure you have the following installed and set up:

* A Kubernetes cluster (Kind, Minikube, or a managed cluster)
* `kubectl` CLI configured for your cluster
* Docker installed locally
* Docker Hub account or any other image registry (used for pushing container images)

---

## 🗂 Project Structure

```
/blue-green-deployment
├── /app
│   └── server.sh               # Basic HTTP server script with version info
│
├── /manifests                  # Kubernetes manifests
│   ├── blue-deployment.yaml    # Blue (stable) version of the app
│   ├── green-deployment.yaml   # Green (new) version of the app
│   └── service.yaml            # Service resource to control traffic
│
├── Dockerfile                  # Container definition for the app
└── README.md                   # This documentation
```

---

## 🚀 How to Use

### 1. **Build and Push Container Images**

* Create your app images for each version.
* Push them to your Docker Hub (or other) registry.

  * You will need two versions: one for **v1** (blue) and one for **v2** (green).
  * Tag them clearly (`v1.0`, `v2.0`, etc.).

### 2. **Update Image References**

* Replace `YOUR_DOCKER_USERNAME` in the manifest files (`blue-deployment.yaml`, `green-deployment.yaml`) with your actual Docker Hub username or image path.

### 3. **Deploy Blue Version**

* Apply the **blue deployment** and **service**:

  ```sh
  kubectl apply -f manifests/blue-deployment.yaml
  kubectl apply -f manifests/service.yaml
  ```

### 4. **Verify Deployment**

* In a second terminal, run a temporary curl pod in your cluster to test the response:

  ```sh
  kubectl run curl --image=alpine/curl:8.2.1 -n kube-system -it --rm -- sh
  ```
* Inside the pod, run:

  ```sh
  for i in `seq 1 1000`; do curl myapp.default:8000/; echo ""; sleep 1; done
  ```
* You should see output indicating version **v1**.

### 5. **Deploy Green Version**

* Apply the green deployment:

  ```sh
  kubectl apply -f manifests/green-deployment.yaml
  ```

* You'll notice that the `curl` terminal is still printing **v1**

### 6. **Switch Traffic to Green**

* Edit `service.yaml` to point the `selector` from `replica: blue` to `replica: green`.
* Apply the updated service:

  ```sh
  kubectl apply -f manifests/service.yaml
  ```
* Now traffic should be routed to the green version (**v2**).

### 7. **Rollback if Needed**

* To revert to the blue version, update the `service.yaml` selector back to `replica: blue` and re-apply it.

---

## 🧹 Cleanup

To remove all resources:

```sh
kubectl delete deployment green-myapp
kubectl delete deployment blue-myapp
kubectl delete service myapp
```

---

## ➕ Next Steps

Here are some ways you can expand this project:

* Add a CI/CD pipeline (e.g., GitHub Actions)
* Automate image builds and deployments
* Implement advanced routing with **Ingress**
* Add health checks and automatic rollbacks

---
