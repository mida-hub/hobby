# setup
brew install kubernetes-helm

# argo workflows
helm repo add argo https://argoproj.github.io/argo-helm
helm search repo argo
helm install argo argo/argo-workflows
kubectl port-forward deployment.apps/argo-argo-workflows-server 2746:2746
kubectl exec -it $(kubectl get --no-headers=true pods -o name | grep server) -- argo auth token

helm pull argo/argo-workflows
tar xvzf argo-workflows-0.17.0.tgz

# custom chart
helm create mychart
helm install mychart ./mychart
helm install mychart ./mychart --debug --dry-run
