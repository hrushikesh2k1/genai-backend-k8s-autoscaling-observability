# genai-backend-k8s-autoscaling-observability
Production-style GenAI backend built with FastAPI, containerized with Docker, deployed on Kubernetes, horizontally autoscaled using CPU-based HPA, and monitored using Prometheus and Grafana. This project demonstrates end-to-end backend engineering, Kubernetes autoscaling, metrics-driven scaling decisions, and observability.

Step 1:
Develop the back-end using FastAPI that mimics the Gen AI behaviour. The code is provided in repo.
To run the back-end, run the below cmd.
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Go to local browser and search for localhost:8000/docs which shows list of api's to access.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3c58715c-b7a9-4146-9c42-e9f892c7d308" />
When you check /health endpoint, it should return status as 'ok'. You can also test /generate endpoint.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4bd7ea63-fe6c-4706-bedb-ea66c43f57d5" />

So, Now the back-end is ready. Now, we can containarize it.

Step 2:
-->For containerizig the application, we write the Dockerfile which is provided in the repo.
-->After writing the Dockerfile, build the image, push it into docker hub and run the container.
-->I am using docker desktop for the above.
Building the image
```
docker build -t hrushikesh2k1/genai-service:v1 .
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/66551076-584a-4a61-9d94-2a267e3341e5" />

Running the container
```
docker run -d -p 8000:8000 -e USE_MOCK_AI=true hrushikesh2k1/genai-service:v1
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f03df922-fcb8-4d06-ac13-86494892d19f" />
You can see the application running on port 8000 on your localhost.

Step 3:
-->Deployig the application to kubernetes in docker desktop. Create the k8s cluster. After that create a folder called k8s at the root and create folders called deployment.yaml, service.yaml and hpa.yaml.
-->Apply all the manifests
```
kubectl apply -f k8s/
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/83ac0c16-70d6-40c6-92cb-a7a6f2b53773" />
-->You can see the cpu usage in hpa service, as we targeted CPU usage itself. The CPU info is given to hpa (Horizontal Pod Auto-scaler) by metrics-server.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5dfaca69-b9e5-43ab-aa4d-70b857250a4e" />
-->Tested the HPA by serving the load to application with while loop in another terminal and watching hpa service live. Below the hpa scaled up to 4 replicas.
```
while true; do curl -s http://localhost:30007/health > /dev/null; done
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/29c71489-1f82-4d78-b3ba-8468e726aa3e" />
-->Scaling down takes minutes because system will scale down after checking stability in cpu usage.
HPA
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d2dc9ac7-eff2-48e4-8444-1b8385805632" />
Pods
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3e8d883f-806a-4c69-8a32-b717f3376d73" />



step 4:
-->Build the monitoring system using prometheus and grafana.
-->I am installing prometheus stack using helm, so you need to have helm installed.
-->To install prometheus and grafana
```
# Add the helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install prometheus stack, this installs prometheus and grafana under monitoring namespace
helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
```
To access grafana and dashboards, we use port-forward for simplicity rather than having ingress installed for exposing.
```
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```
Click on Import dashboard> enter the ID: 15757 for pod dashboard
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/57d93314-9c6a-41a1-aab5-8528e2282140" />
The below dashboard is for Pods
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7927d241-8fd1-43fc-b811-ae78735cc3c4" />
Below is for hpa
