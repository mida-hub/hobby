FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    curl \
    nginx \
    cvs
# 検証中はRUNを複数
# 最後にひとつにまとめる
# RUN apt-get install -y cvs

# CMD ["ls"]
# CMD ["pwd"]
CMD ["/bin/bash"]
