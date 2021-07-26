# dockerfile-recover
dockerfile-recover is a tool to reconstruct Dockerfile by reverse engineering a docker image

# Installation

## With pip
```
pip install dockerfile-recover
```
## In a container
```
docker pull purificant/dockerfile-recover
```

# Usage

## When installing with pip
```
docker pull <the image you want to reverse engineer>
dockerfile-recover <image name>
```
For example
```
dockerfile-recover python
dockerfile-recover django
dockerfile-recover redis
dockerfile-recover node
```

or run as python module
```
python -m dockerfile_recover nginx
```

## When running in a container

```
docker pull <the image you want to reverse engineer>
docker run -it -v /var/run/docker.sock:/var/run/docker.sock purificant/dockerfile-recover python -m dockerfile_recover <image name>
```