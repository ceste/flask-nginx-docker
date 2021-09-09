[![Dockerize FLask App with Nginx](https://github.com/ceste/flask-nginx-docker/actions/workflows/main.yml/badge.svg)](https://github.com/ceste/flask-nginx-docker/actions/workflows/main.yml)

# flask-nginx-docker

## Build Image

```
docker build -t my_image .
```

## Build Container

```
docker run -d --name my_container -p 5001:5001 my_image
```

## CURL Get Method

```
curl localhost:5001
```

## CURL Post Method (does not work)

``` 
curl -X POST -H 'Accept: application/json' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 19' -H 'Content-type: application/json' -H 'User-Agent: python-requests/2.26.0' -d '{"name" :"Chandra"}' http://127.0.0.1:5001/call
```

```
curl -v -XPOST -H "Content-type: application/json" -d '{"name":"chandra"}' 'http://localhost:5001/call'
```



Does not work


