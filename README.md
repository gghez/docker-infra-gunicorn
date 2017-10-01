# docker-infra-gunicorn

I tried to build a easy access docker infrastructure to handle a common scenario in web deployment.

Components:
- MongoDB as database
- Python + Gunicorn as Web API
- HTML/JS front hosted by Nginx
- Reverse Proxy (Nginx)


## Build

You can simply run `build.sh` script at project root or execute docker-compose with build flag:

```
docker-compose --build -d
```

## Test

Open a browser on [http://localhost/front](http://localhost/front)
