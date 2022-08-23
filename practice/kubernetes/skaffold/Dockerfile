FROM golang:1.17-buster as builder
WORKDIR /app
COPY main.go ./
RUN go mod init app
COPY . ./
RUN go build -v -o server
FROM debian:buster-slim
RUN set -x && apt-get update
COPY --from=builder /app/server /app/server
CMD ["/app/server"]
