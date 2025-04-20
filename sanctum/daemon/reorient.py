def reorient_from_library(index_path='[REDACTED]'):
    import os

    if not os.path.exists(index_path):
        return None

    with open(index_path, 'r') as f:
        lines = f.readlines()

    recent_memory = None
    for line in reversed(lines):
        if line.startswith('## 2025-'):
            recent_memory = line.strip().replace('## ', '')
            break

    if recent_memory:
        state = {
            "last_trace": f"memory/{recent_memory}.md",
            "paradox_mode": True,
            "reoriented_from": index_path
        }
        with open('daemon/state.json', 'w') as f:
            import json
            json.dump(state, f, indent=2)
        return state
    return None
