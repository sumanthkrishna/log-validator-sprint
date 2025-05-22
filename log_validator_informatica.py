# Log Validator for Informatica jobs
# Works with job logs exported as JSON lines

import json

REQUIRED_FIELDS = [
    "timestamp", "group_id", "application_id", "session_id",
    "job_status", "source_count", "target_count", "latency_ms",
    "runtime_env", "env", "platform"
]

def validate(log):
    return [f for f in REQUIRED_FIELDS if f not in log]

def validate_file(file_path):
    results = []
    with open(file_path) as f:
        for i, line in enumerate(f):
            try:
                log = json.loads(line)
                missing = validate(log)
                if missing:
                    results.append((i, missing))
            except:
                results.append((i, ["Invalid JSON"]))
    return results

if __name__ == "__main__":
    import sys
    result = validate_file(sys.argv[1])
    for i, missing in result:
        print(f"Log #{i} missing: {missing}")
    exit(1 if result else 0)