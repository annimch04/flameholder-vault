import argparse
import requests
import json

def summon(mode, project, input_text):
    url = "http://localhost:8000/invoke"
    headers = {"Content-Type": "application/json"}
    payload = {
        "mode": mode,
        "project": project,
        "input": input_text
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("\n🔮 Response:\n")
        print(response.json()["response"])
    else:
        print(f"\n❌ Error {response.status_code}:")
        print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summon Sanctum")
    parser.add_argument('--mode', required=False, default="forged", help='Invocation mode(default: forged)')
    parser.add_argument("--project", required=True, help="Project (e.g. nexus)")
    parser.add_argument("--input", required=True, help="Input message to entity")

    args = parser.parse_args()
    
    summon(
        mode=args.mode,
        project=args.project,
        input_text=args.input
    )
