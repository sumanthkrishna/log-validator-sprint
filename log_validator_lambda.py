# AWS Lambda Log Validator
# Targets JSON logs from CloudWatch or exported tools

import json

REQUIRED = [
    "timestamp", "group_id", "application_id", "execution_id",
    "status", "duration_ms", "memory_used_mb", "cold_start",
    "trigger_source", "env", "region", "platform"
]

def validate(log):
    return [f for f in REQUIRED if f not in log]

def validate_file(file_path):
    issues = []
    with open(file_path) as f:
        for idx, line in enumerate(f):
            try:
                log = json.loads(line)
                missing = validate(log)
                if missing:
                    issues.append((idx, missing))
            except:
                issues.append((idx, ["Invalid JSON"]))
    return issues

if __name__ == "__main__":
    import sys
    result = validate_file(sys.argv[1])
    for i, missing in result:
        print(f"Line {i}: Missing fields {missing}")
    exit(1 if result else 0)