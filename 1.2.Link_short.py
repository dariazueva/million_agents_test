import hashlib
from http.client import HTTPException

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
url_store: dict[str, str] = {}


class UrlRequest(BaseModel):
    original_url: str


def generate_short_url(original_url: str) -> str:
    short_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
    return short_url


@app.post("/shorten")
async def shorten_url(request: UrlRequest):
    original_url = request.original_url
    short_url = generate_short_url(original_url)
    url_store[short_url] = original_url
    return {"short_url": f"http://127.0.0.1:8000/{short_url}"}


@app.get("/{short_url}")
async def redirect_to_original(short_url: str):
    original_url = url_store.get(short_url)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": original_url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
