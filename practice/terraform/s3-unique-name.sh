#!/bin/bash

DNS=`echo $1 | grep -cwE '^[a-z0-9][a-z0-9\.\-]{1,61}[a-z0-9]$'` # S3バケット名の使用可能文字および文字数を守っているか

if [ ${DNS} -eq 0 ];then
    echo "半角小文字英数字とハイフン以外の文字を使っている、バケット名の先頭または末尾が小文字の英数字でない、または3文字以上63文字以下になってない可能性があります"
    exit
fi

IPADDR=`echo $1 | grep -cwE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'` # S3バケット名がIPアドレス形式(XXX.XXX.XXX.XXX)でないか

if [ $IPADDR -eq 1 ];then
    echo "S3バケット名にIPアドレス形式は使用できません"
    exit
fi

CONTSYMBOL=`echo $1 | grep -cE '\.{2,}'` # S3バケット名にピリオドが連続していないか

if [ $CONTSYMBOL -eq 1 ];then
    echo "ピリオドが連続しています"
    exit
fi

UNIQUE=`aws s3api head-bucket --bucket $1 2>&1 | grep -cE '404'` # 命名規則に則った上での404エラーはバケットが存在しなくて作成可能だとみなす

if [ $UNIQUE -eq 0 ];then
    echo "重複するS3バケット名が存在しています"
    exit
fi

PERIOD=`echo $1 | grep -cE '\.'` # ピリオドが含まれている場合に警告する

if [ $PERIOD -eq 1 ];then
    echo "$1はユニークなS3バケット名ですがピリオドが含まれているとSSLワイルドカード証明書が使えなくなる為、ピリオド抜きに変更をお勧めします"
    exit
fi
# 以下、ユニークなS3バケット名でバケットを作成するか選べる
echo "$1はユニークなS3バケット名です。バケットを作成する場合はyesと入力して下さい:"
read -p "Make S3 Bucket?:" S3MAKE

if [ "$S3MAKE" = yes ];then
    aws s3 mb s3://$1
else
    exit
fi