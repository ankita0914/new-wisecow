### **README.md**

````markdown
<p align="center">
<img src="https://i.imgur.com/uG9Xy9l.png" alt="WiseCow Logo">
</p>

# **Wisecow Application**

The **Wisecow** application is a simple, lightweight utility that combines a fortune cookie message with a text-based cow image, all packaged and deployed as a modern, containerized application. It's a fun project to demonstrate a complete development and deployment lifecycle, from initial coding to CI/CD automation.

## **Features**

- 💬 **Random Fortunes**: Serves a different "fortune" with every run.
- 🐄 **ASCII Art**: Uses `cowsay` to display the fortune in a whimsical cow image.
- 📦 **Containerized**: Fully packaged in a Docker image for easy portability.
- 🚀 **Orchestrated**: Deployed on Kubernetes for scalability and management.
- ⚙️ **Automated CI/CD**: Utilizes GitHub Actions for an automated build, push, and deployment pipeline.

## **Getting Started**

### **Prerequisites**

- **Git**: For cloning the repository.
- **Docker**: For building and running the container.
- **kubectl**: For interacting with the Kubernetes cluster.

### **1. Clone the Repository**

```bash
git clone https://github.com/ankita0914/new-wisecow.git
cd new-wisecow
````

### **2. Dockerize the Application**

The application uses a `Dockerfile` to create a Docker image.

```bash
docker build -t wisecow:latest .
```

You can run it locally to test:

```bash
docker run -d --name wisecow -p 5000:5000 wisecow:latest
```

### **3. Deploy to Kubernetes**

Navigate to the `kubernetes` directory to find the deployment manifests:

```bash
cd kubernetes
```

Apply the Kubernetes manifests to deploy the application:

```bash
kubectl apply -f namespace.yaml
kubectl apply -f wisecow-deployment.yaml -n wisecow-namespace
kubectl apply -f wisecow-service.yaml -n wisecow-namespace
kubectl apply -f wisecow-ingress.yaml -n wisecow-namespace
```

Check the status of your pods and services:

```bash
kubectl get pods -n wisecow-namespace
kubectl get services -n wisecow-namespace
```

### **4. CI/CD with GitHub Actions**

This repository includes a GitHub Actions workflow located at `.github/workflows/ci-cd-wisecow.yml`. This workflow is triggered on every push to the `main` branch and automates:

1. **Build** the Docker image.
2. **Push** the image to Docker Hub.
3. **Deploy** the new version to the Kubernetes cluster.

## **Contribution**

Feel free to open an issue or submit a pull request if you'd like to contribute!

```

---

### **Project Structure**

```

new-wisecow/
├── Dockerfile
├── LICENSE
├── README.md
├── kubernetes/
│   ├── namespace.yaml
│   ├── wisecow-deployment.yaml
│   ├── wisecow-service.yaml
│   ├── wisecow-ingress.yaml
│   ├── kubearmor-ds.yaml
│   └── kubearmor-wisecow-policy.yaml
├── wisecow\.sh
└── .github/
└── workflows/
└── ci-cd-wisecow\.yml

### ***Output Images***
<img width="1315" height="496" alt="Screenshot 2025-09-21 043827" src="https://github.com/user-attachments/assets/92425bb5-c47d-4100-ac46-a33c21f90903" />
<img width="819" height="217" alt="Screenshot 2025-09-21 181819" src="https://github.com/user-attachments/assets/0449870f-f811-47f1-a02c-4365cacd31d3" />
<img width="1863" height="954" alt="Screenshot 2025-09-21 033047" src="https://github.com/user-attachments/assets/c4d4f4a9-7d59-4aa3-af4f-05bf9655e1d2" />
<img width="1919" height="1023" alt="Screenshot 2025-09-21 020046" src="https://github.com/user-attachments/assets/b331936b-434c-4c14-b094-723903182d3e" />
<img width="943" height="305" alt="Screenshot 2025-09-21 043754" src="https://github.com/user-attachments/assets/d0ec5d60-cdce-424e-8d07-4ec8f606f3ec" />




