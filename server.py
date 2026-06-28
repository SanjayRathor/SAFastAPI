# server.py
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

BASE_URL = "https://jsonplaceholder.typicode.com"

@app.get("/posts")
async def get_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts")
        return response.json()

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts/{post_id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Post not found")
        return response.json()
    

    