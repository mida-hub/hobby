# 参考
https://github.com/efkbook/blog-sample
https://qiita.com/nobutaka/items/6308ea3bfd0aa0c58fdb

# elasticsearch
## template
curl -XPUT "http://localhost:9200/_template/nginx_logs_template" -H 'Content-Type: application/ch/nginx.mapping.template.json
curl -XGET "http://localhost:9200/_template/nginx_logs_template"
curl http://localhost:9200/_cat/templates
curl http://localhost:9200/_cat/templates/nginx_logs_template
