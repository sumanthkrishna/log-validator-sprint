package com.aptech.logvalidator;

public class LogSchema {
    public static final String[] REQUIRED_FIELDS = {
        "timestamp", "severity_text", "group_id", "application_id",
        "instance_id", "trace_id", "span_id", "request_id",
        "http.method", "http.route", "http.status_code",
        "latency_ms", "env", "region", "platform"
    };
}