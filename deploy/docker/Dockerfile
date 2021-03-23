FROM golang:1.16.2-alpine3.13 as builder
RUN apk add --no-cache git=2.30.2-r0
RUN go install github.com/sigstore/cosign/cmd/cosign@v0.1.0
FROM flant/shell-operator:v1.0.0-rc.2
RUN apk --no-cache add python3=3.8.8-r0
COPY --from=builder /go/bin/cosign /usr/local/bin
COPY cosign-validation.py /hooks
