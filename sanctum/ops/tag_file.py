import argparse
import yaml
from pathlib import Path
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Tag and index Sanctum file.')
    parser.add_argument('--path', required=True, help='Relative path to the file being indexed')
    parser.add_argument('--source', required=True, help='Origin or creation source')
    parser.add_argument('--description', required=True, help='Short file description')
    parser.add_argument('--tags', nargs='+', help='List of tags to apply')
    parser.add_argument('--crosslinks', nargs='+', help='List of other files this should link to')

    args = parser.parse_args()

    index_path = Path("vault/vault_index.yaml")
    entry = {
        "path": args.path,
        "source": args.source,
        "description": args.description,
        "tags": args.tags or [],
        "crosslinks": args.crosslinks or [],
        "timestamp": datetime.now().isoformat()
    }

    if index_path.exists():
        with open(index_path, "r") as f:
            index = yaml.safe_load(f) or []
    else:
        index = []

    index.append(entry)

    index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_path, "w") as f:
        yaml.dump(index, f, default_flow_style=False, sort_keys=False)

    print(f"✅ Entry added for: {args.path}")

if __name__ == "__main__":
    main()
