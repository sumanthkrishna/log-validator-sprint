package com.aptech.logvalidator;

import java.io.File;

public class LogValidatorMain {
    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: java -jar log-validator.jar <log-file-path>");
            System.exit(1);
        }

        File logFile = new File(args[0]);
        boolean result = LogValidator.validateFile(logFile);

        if (result) {
            System.out.println("✅ All logs passed validation.");
            System.exit(0);
        } else {
            System.err.println("❌ Log validation failed. See above for details.");
            System.exit(1);
        }
    }
}