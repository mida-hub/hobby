git clone https://github.com/airbytehq/airbyte.git
cd airbyte
kubectl apply -k kube/overlays/stable
kubectl port-forward svc/airbyte-webapp-svc 8000:80
