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
dockerfile-recover recover IMAGE_NAME
```
Optionally `--pull` the image, for example:
```
dockerfile-recover recover --pull python
dockerfile-recover recover --pull django
dockerfile-recover recover --pull redis
dockerfile-recover recover --pull node
```

or run as python module
```
python -m dockerfile_recover recover --pull nginx
```

## When running in a container

```
docker run -it -v /var/run/docker.sock:/var/run/docker.sock purificant/dockerfile-recover python -m dockerfile_recover recover IMAGE_NAME
```
