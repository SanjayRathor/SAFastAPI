# client.py
import requests
import json

BASE = "http://127.0.0.1:8000"

def pretty(data):
    print(json.dumps(data, indent=2))

# Get all posts
print("\n── All Posts ──")
res = requests.get(f"{BASE}/posts")
posts = res.json()
print(f"Total posts fetched: {len(posts)}")
pretty(posts[:2])  # show first 2

# Get single post
print("\n── Post #1 ──")
res = requests.get(f"{BASE}/posts/1")
pretty(res.json())

# Get a post that doesn't exist
print("\n── Post #999 (should 404) ──")
res = requests.get(f"{BASE}/posts/999")
print(f"Status: {res.status_code}")
print(res.json())