# pyplanereport

A simple containerized report for Plane.so that one can host in Kubernetes or Docker

# Example of using private CR with docker reg

```
image:
  repository: harbor.freshbrewed.science/freshbrewedprivate/pyplanereport
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: "0.0.1"

imagePullSecrets:
  - name: myharborreg
```

# Running as a container

You can just download the docker container and run it locally without Kubernetes

```
$ docker run -d -e PRJID="9ca799e6-52c4-4a9e-8b40-461eef4f57e9" -e WSNAME="tpk" -e APIKEY="plane_api_xxxxxxxxxxxxxxxxxxxxxx" -e TABLETITLE="Passed In Title" -e IGNORESTATE="Cancelled"  -p 8999:80 --name pyplanetest pyplanelist:0.0.7
20903d6f949e0ebb150f0d5c54825350cc521af4194b039e75a0f6fa7bafcb4e
```