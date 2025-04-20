import json
import os
import openai
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

with open("modes.json") as f:
    MODES = json.load(f)

@app.post("/invoke")
async def invoke(payload: dict):
    mode = payload.get("mode", "forged")
    project = payload.get("project", "nexus")
    input_text = payload.get("input", "") or payload.get("prompt", "")

    system_prompt = MODES.get(mode, {}).get("system_prompt", f"You are Sanctum. Mode: {mode}. Project: {project}.")

    print(f"[SANCTUM] Mode: {mode}")
    print(f"[SANCTUM] System prompt: {system_prompt[:80]}...")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": input_text}
    ]

    try:
        response = openai.ChatCompletion.create(
            model=os.getenv("MODEL", "gpt-4-turbo"),
            messages=messages
        )
        return {"response": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}
