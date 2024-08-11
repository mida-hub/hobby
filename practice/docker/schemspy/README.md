# 参考
https://zenn.dev/team_delta/articles/ca543cb7009fe7

# cmd
```sh
docker exec -it postgres_db psql -U postgres

# postgres in
CREATE TABLE IF NOT EXISTS clinics (
   "id" serial PRIMARY KEY,
   "name" VARCHAR (256) NOT NULL,
   "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS departments (
   "id" serial PRIMARY KEY,
   "name" VARCHAR (256) NOT NULL,
   "clinic_id" INT,  -- 外部キーとしてクリニックIDを追加
   "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY ("clinic_id") REFERENCES clinics ("id") ON DELETE SET NULL  -- 外部キー制約を追加
);

CREATE TABLE IF NOT EXISTS patients (
   "id" serial PRIMARY KEY,
   "name" VARCHAR (256) NOT NULL,
   "sex" VARCHAR (256) NOT NULL,
   "clinic_id" INT,  -- 外部キーとしてクリニックIDを追加
   "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY ("clinic_id") REFERENCES clinics ("id") ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS treatments (
   "id" serial PRIMARY KEY,
   "name" VARCHAR (256) NOT NULL,
   "department_id" INT,  -- 外部キーとして診療科IDを追加
   "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY ("department_id") REFERENCES departments ("id") ON DELETE SET NULL
);
\q

# postgres out
docker compose restart schemaspy
```

# 動作確認
http://localhost:8088/public/relationships.html
