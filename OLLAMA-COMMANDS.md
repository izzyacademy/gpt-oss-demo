
## Commands to Pull down GPT OSS via REST API

````bash

## grab llama 3.2
curl http://192.168.86.43:11434/api/pull -d '{
  "model": "llama3.2"
}'

## grab gpt-oss:20b
curl http://192.168.86.43:11434/api/pull -d '{
  "model": "gpt-oss:20b"
}'

````