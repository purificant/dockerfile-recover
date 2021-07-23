# dockerfile-recover
dockerfile-recover is a tool to reconstruct Dockerfile by reverse engineering a docker image

# Installation
```
pip install dockerfile-recover
```

# Usage

```
docker pull <the image you want to reverse engineer>
dockerfile-recover <image name>
```
For example
```
dockerfile-recover python
```
