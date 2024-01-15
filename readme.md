# fastapi-load-test-example

Build container
```sh
docker build -t fastapi-transformer .
```

Start container in interactive mode
```sh
docker run -it -p9000:9000 fastapi-transformer bash
```

Run command within container
```sh
uvicorn main:app --host 0.0.0.0 --port 9000
```

