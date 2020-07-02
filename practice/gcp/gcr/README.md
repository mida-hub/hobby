gcloud auth configure-docker
docker build -f Dockerfile --tag=gcr.io/project-id/sample:latest .
docker push gcr.io/project-id/sample:latest
