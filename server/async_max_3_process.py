import asyncio
import functools
import time
from concurrent.futures import ThreadPoolExecutor
import uvicorn

from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel

# if you try to run all predicts concurrently, it will result in CPU trashing.
pool = ThreadPoolExecutor(max_workers=3)

app = FastAPI()

sbertmodel = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')


class Input(BaseModel):
    text: str


def model_predict(text: str):
    ts = time.time()
    vector = sbertmodel.encode(sentences=[text])
    print(f"Inner model  : {int((time.time() - ts) * 1000)}ms")
    return vector


@app.post("/")
async def entrypoint(input: Input):
    loop = asyncio.get_event_loop()
    ts = time.time()
    vector = await loop.run_in_executor(pool, functools.partial(model_predict, text=input.text))
    return {"response": vector.tolist()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)