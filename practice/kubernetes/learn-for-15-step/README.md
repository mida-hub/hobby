# Step 6
```
# クラスタ構成の確認
kubectl cluster-info
# クラスタのノード表示
kubectl get node
# ポッドの実行
kubectl run hello-world --image=hello-world -it --restart=Never --rm
# ポッドの表示
kubectl get pod
# ポッドの削除
kubectl delete pod hello-world
# ポッドのログを表示
kubectl logs hello-world

# ウェブサーバー 自己回復
kubectl run webserver --image=nginx --replicas=5
kubectl delete po webserver-666c4ccf4d-2bfhr webserver-666c4ccf4d-dn9dw
kubectl get deploy,po
kubectl delete deployment webserver

# ジョブ制御下でのポッド実行
kubectl run hello-world --image=hello-world --restart=OnFailure
kubectl create job hello-world --image=hello-world

# ポッドの終了コードによるコントローラーの振る舞いの違い
kubectl create job job-1 --image=ubuntu -- /bin/bash -c "exit 0"
kubectl create job job-2 --image=ubuntu -- /bin/bash -c "exit 1"
kubectl get po
```
