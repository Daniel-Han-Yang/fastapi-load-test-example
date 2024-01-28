# fastapi-load-test-example

Build container
```sh
docker build -t fastapi-transformer .
```

Start container in interactive mode
GPU
```sh
docker run --gpus=1 -it -p9000:9000 -v $PWD/server:/app/server/ fastapi-transformer bash
```

CPU
```sh
docker run -it -p9000:9000 fastapi-transformer bash
```

Run command within container
```sh
cd server
uvicorn async_fast_1:app --host 0.0.0.0 --port 9000
```


async_max_2_process setup seems to be the most performant when testing with GPU.

