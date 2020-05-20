#!/bin/bash

# project_id は明示的に固定しておく
project_id=hogehoge
dataset_id=$1

# cf. https://qiita.com/okisanjp/items/7985ddb9b1b00f1617a9
# mac は /bin/echo としないと -n がうまく動作しない
/bin/echo -n "bq rm ${project_id}:${dataset_id}.tables? [y/n]"
read answer

if [ "$answer" = "y" ]; then

  # 明示的に区切り文字を改行コードにする
  IFS=$'\n';
  # bq ls dataset | TABLE行のみ取得 | TABLE以降の文字列を削除 | 空白削除
  for LINE in `bq ls ${project_id}:${dataset_id} | grep TABLE | sed 's/TABLE.*//g' | sed 's/ //g '`
  do
    yes | bq rm ${project_id}:${dataset_id}.${LINE}
  done

fi


