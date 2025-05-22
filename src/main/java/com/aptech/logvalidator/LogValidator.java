package com.aptech.logvalidator;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.*;
import java.util.*;

public class LogValidator {

    private static final ObjectMapper objectMapper = new ObjectMapper();

    public static List<String> validateLog(JsonNode log) {
        List<String> missingFields = new ArrayList<>();
        for (String field : LogSchema.REQUIRED_FIELDS) {
            if (!log.has(field)) {
                missingFields.add(field);
            }
        }
        return missingFields;
    }

    public static boolean validateFile(File logFile) throws IOException {
        boolean allValid = true;
        BufferedReader reader = new BufferedReader(new FileReader(logFile));
        String line;
        int lineNumber = 1;
        while ((line = reader.readLine()) != null) {
            JsonNode log = objectMapper.readTree(line);
            List<String> missing = validateLog(log);
            if (!missing.isEmpty()) {
                allValid = false;
                System.out.printf("Log line %d missing fields: %s%n", lineNumber, String.join(", ", missing));
            }
            lineNumber++;
        }
        return allValid;
    }
}