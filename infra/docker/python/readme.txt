docker build .
docker image ls
docker run -p 8888:8888 -v :/work --name my-lab 8257c54503ec
