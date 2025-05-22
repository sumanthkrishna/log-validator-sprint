# Log Validator for Ab Initio logs
# Assumes log entries are stored in a structured flat file format or log.txt

import json

REQUIRED_FIELDS = [
    "timestamp", "group_id", "application_id", "job_status",
    "start_time", "end_time", "source_count", "target_count", "env", "platform"
]

def validate_log_entry(log):
    missing = [f for f in REQUIRED_FIELDS if f not in log]
    return missing

def validate_file(file_path):
    results = []
    with open(file_path) as f:
        for i, line in enumerate(f):
            try:
                log = json.loads(line)
                missing = validate_log_entry(log)
                if missing:
                    results.append((i, missing))
            except:
                results.append((i, ["Invalid JSON"]))
    return results

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    failures = validate_file(path)
    for i, fields in failures:
        print(f"Line {i}: Missing fields: {fields}")
    exit(1 if failures else 0)