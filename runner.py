"""Single non-streaming request to local Ollama. No loop, no history, no retry."""
from __future__ import annotations

import argparse
import json
import urllib.request

from loader import load_context

MODEL = "gemma3:4b"
OLLAMA_URL = "http://localhost:11434/api/chat"
TIMEOUT_SECONDS = 120


def run(domain: str, query: str) -> None:
    system = load_context(domain)
    payload = {
        "model": MODEL,
        "stream": False,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": query},
        ],
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
        data = json.loads(resp.read())
    print(data["message"]["content"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="SARA CLI — single Ollama request, exits after response"
    )
    ap.add_argument(
        "domain",
        help="Operator domain: morning | lesson | review | weekly | indranet | goals | code | general",
    )
    ap.add_argument("query", help="Your prompt to SARA")
    args = ap.parse_args()
    run(args.domain, args.query)
