from fastapi import FastAPI
import requests
import os

app = FastAPI()

HA_URL = "http://supervisor/core"
HA_TOKEN = os.environ.get("HA_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

@app.get("/tools/get_state")
def get_state(entity_id: str):
    r = requests.get(
        f"{HA_URL}/api/states/{entity_id}",
        headers=HEADERS,
        timeout=5,
    )
    return r.json()

@app.post("/tools/call_service")
def call_service(domain: str, service: str, entity_id: str):
    r = requests.post(
        f"{HA_URL}/api/services/{domain}/{service}",
        headers=HEADERS,
        json={"entity_id": entity_id},
        timeout=5,
    )
    return {"status": "ok"}
