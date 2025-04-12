FROM golang:1.20-alpine

WORKDIR /app
COPY . .

RUN apk add --no-cache make git bash build-base
RUN make install

EXPOSE 26656 26657

CMD ["mhdd", "start"]