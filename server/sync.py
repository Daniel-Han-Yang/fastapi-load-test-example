import time
import uvicorn

from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel

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
def entrypoint(input: Input):
    return {"response": model_predict(input.text).tolist()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
