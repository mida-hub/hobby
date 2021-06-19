```
docker build -t test-image ./
docker run -it -d --name="api-container" test-image
docker run -it -d --name="curl-container" test-image

docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' api-container
docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' api-container
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' curl-container
docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' curl-container

docker exec -it curl-container sh

brctl show docker0
```
