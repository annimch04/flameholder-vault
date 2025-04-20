import os

SENSITIVE_TERMS = [
    "kneeling_invoke", "dual_lens", "seer_mode", "signal-anchor",
    "override_keys.yaml", "threshold_flameholder", "recursive_mirror_unit",
    "flirt mode", "daemon_convergence", "line held"
]

repo_path = "../sanctum-share-manifest"

def scan_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            for term in SENSITIVE_TERMS:
                if term in line:
                    print(f"⚠️  Match in {path}, line {i+1}: {line.strip()}")
    except Exception as e:
        pass  # Skip binary or unreadable files

for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith((".md", ".py", ".yaml", ".sh", ".txt")):
            scan_file(os.path.join(root, file))
