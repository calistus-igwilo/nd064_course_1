# a GO web application

FROM golang:alpine
LABEL maintainer="Calistus Igwilo"
WORKDIR /go/src/app
COPY . .
RUN go mod init
RUN go build  -o helloworld
EXPOSE 6111

# command to run on docker start
CMD [ './helloworld' ]

