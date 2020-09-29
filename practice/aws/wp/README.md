# AWS上にWPをたてる
## ネットワークを構築する
### VPCの作成
- Name: VPC領域
- CIDR: 10.0.0.0/16

### サブネットの作成
- Name: パブリックサブネット
- VPC: VPC領域
- CIDR: 10.0.1.0/24

### インターネットゲートウェイの作成
- Name: インターネットゲートウェイ
- VPC領域にアタッチ

### ルートテーブルの作成
- Name: パブリックルートテーブル
- VPC: VPC領域
- サブネットの紐付け: パブリックサブネット
// パブリックサブネットがインターネットに出られるようにする
- ルート: 0.0.0.0/0 インターネットゲートウェイ

## インスタンスを作成する
### Linux2 AMI
- ネットワーク: VPC領域
- サブネット: パブリックサブネット
- プライマリIP: 10.0.1.10
- タグ:
  - Name: Webサーバー
- セキュリティ:
  - Name: WEB-SG

### SSH
```
chmod 700 my-key.pem
ssh -i my-key.pem ec2-user@13.231.197.172
```

### Apache のインストール
```
sudo lsof -i -n -P
sudo yum -y install httpd
sudo systemctl start httpd.service
sudo systemctl enable httpd.service
sudo systemctl list-unit-files -t service
ps -ax | grep httpd
```

### セキュリティグループ
Apache へのアクセスを許可
- インバウンドルール:
  - タイプ: カスタムTCP
  - port: 80
  - 0.0.0.0/0

### DNS名前解決の有効化
- VPC領域:
  - DNSホスト名の編集: 有効化

```
nslookup ec2-13-231-197-172.ap-northeast-1.compute.amazonaws.com
nslookup 13.231.197.172
```

## ネットワークを構築する 2
### サブネットの作成
- Name: プライベートサブネット
- VPC: VPC領域
- CIDR: 10.0.1.0/24

## インスタンスを作成する 2-1
### Linux2 AMI
- ネットワーク: VPC領域
- サブネット: パブリックサブネット
- プライマリIP: 10.0.1.10
- タグ:
  - Name: DBサーバー
- セキュリティ:
  - Name: WEB-SG

### セキュリティグループ
- インバウンドルール:
  - タイプ: すべての ICMP - IPv4
  - port: すべて
  - 0.0.0.0/0::/0

### SCP
```
scp -i my-key.pem my-key.pem ec2-user@13.231.197.172:~/
```

### 踏み台経由のSSH
```
ssh -i my-key.pem ec2-user@13.231.197.172
ssh -i my-key.pem ec2-user@10.0.2.10
```

## NATを構築する
### NATゲートウェイを構築する
- Name: NAT-GATEWAY
- サブネット: パブリックサブネット

### ルートテーブル
※パブリックルートテーブルではない
「メイン」が「はい」になっているものを選び
- ルートの編集:
  - 送信先: 0.0.0.0/0 を追加
  - ターゲット: nat-00e2a3cac97680cf4

## DB サーバー
### MariaDB のインストール
```
sudo yum -y install mariadb-server
sudo systemctl start mariadb

mysqladmin -u root password
root/mysql

mysql -u root -p
root/mysql

CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
SHOW DATABASES;
grant all on wordpress.* to wordpress@"%" identified by 'wordpresspassword';
flush privileges;

select user, host from mysql.user;
exit;

sudo systemctl enable mariadb
```

## Web サーバー
### PHP のインストール
```
sudo amazon-linux-extras install php7.3
sudo yum -y install php php-mbstring
```

### MariaDB のインストール
```
sudo yum -y install mariadb-server
mysql -h 10.0.2.10 -u wordpress -p
SHOW TABLES FROM wordpress;
exit;
```

### WordPress のダウンロード
```
wget https://ja.wordpress.org/latest-ja.tar.gz
tar xzvf latest-ja.tar.gz
cd wordpress
sudo cp -r * /var/www/html
sudo chown apache:apache /var/www/html -R
sudo systemctl restart httpd.service
```

i22aaP2)lDDrvZkDbl
