# Copy labels to pods from nodes

Built with [Shell Operator](https://github.com/flant/shell-operator)

## Build & Deploy

### Docker Image

~~~command
$ ./build.image.sh [repository:tag]
...
~~~

## Helm install

> cfssl is needed.

~~~command
# Generate certs for 
$ ./gen-certs.sh
...
# Store public keys into the secret.
$ kubectl create secret generic cosign-keys --from-file=cosign.pub
$ helm install cosign-validator .
...
~~~

## Usage

~~~command
# 
~~~

If a namespace has a label like `signed: "required"`, any pods without signature will be rejected.