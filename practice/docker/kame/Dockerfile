FROM ubuntu:latest
# CMD ["ls"]
# CMD ["pwd"]
# CMD ["/bin/bash"]

# ADD 圧縮ファイルをコピーして解凍してくれる
# RUN mkdir /new_dir
# COPY something /new_dir
# ADD compressed.tar /

# 検証中はRUNを複数で良い
# ただ、サイズが大きくなってしまうので最後にRUNをまとめる
# RUN apt-get update && apt-get install -y \
#     curl \
#     nginx \
#     cvs
# RUN apt-get install -y cvs

# ENTRYPOINTでコマンドを固定する docker run で上書きできない
# RUN touch test
# ENTRYPOINT ["ls"]
# CMD ["--help"]

# 環境変数
# ENV key1 value
# ENV key2=value
# ENV key3="v a l u e" key4=v\ a\ l\ u\ e
# ENV key5 v a l u e

# /直下にファイルができる
# RUN mkdir sample_folder
# RUN cd sample_folder
# RUN touch sample_file

# sample_folderの中にできるが毎回このように書くのは大変
# RUN mkdir sample_folder && \
#     cd sample_folder && \
#     touch sample_file

# WORKDIRで作業場所を指定する
RUN mkdir sample_folder
WORKDIR /sample_folder
RUN touch sample_file
