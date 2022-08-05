# setup
https://github.com/argoproj/argo-workflows/releases/tag/v3.3.8

## cli
```
# Download the binary
curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v3.3.8/argo-darwin-amd64.gz

# Unzip
gunzip argo-darwin-amd64.gz

# Make binary executable
chmod +x argo-darwin-amd64

# Move binary to path
mv ./argo-darwin-amd64 /usr/local/bin/argo

# Test installation
argo version
```
## argo workflows
https://argoproj.github.io/argo-workflows/quick-start/

### set up
kubectl create ns argo
kubens argo

kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/quick-start-postgres.yaml

kubectl -n argo port-forward deployment/argo-server 2746:2746

### clean up
kubectl delete -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/quick-start-postgres.yaml

kubectl delete ns argo

## argo job
https://github.com/argoproj/argo-workflows/tree/master/examples

argo submit hello-world.yaml
argo list

argo submit dag-nested.yaml
argo list
