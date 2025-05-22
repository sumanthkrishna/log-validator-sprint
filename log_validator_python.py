# Validator for Python Script / ETL log formats
import json

REQUIRED = [
    "timestamp", "group_id", "application_id", "run_id",
    "stage", "status", "records_processed", "duration_sec",
    "env", "platform"
]

def validate_log(log):
    return [f for f in REQUIRED if f not in log]

def validate_file(path):
    errors = []
    with open(path) as f:
        for idx, line in enumerate(f):
            try:
                log = json.loads(line)
                missing = validate_log(log)
                if missing:
                    errors.append((idx, missing))
            except:
                errors.append((idx, ["Invalid JSON"]))
    return errors

if __name__ == "__main__":
    import sys
    result = validate_file(sys.argv[1])
    for i, missing in result:
        print(f"Line {i}: Missing {missing}")
    exit(1 if result else 0)