/**
 * @file structured-logger.ts
 * @description Production structured JSON logger in TypeScript with correlation IDs.
 * Ingestible by Datadog, Grafana Loki, CloudWatch, and Sentry.
 */

export interface LogContext {
  requestId?: string;
  userId?: string;
  tenantId?: string;
  component?: string;
  [key: string]: any;
}

export class StructuredLogger {
  private static emit(level: "INFO" | "WARN" | "ERROR", message: string, context?: LogContext): void {
    const logEntry = {
      timestamp: new Date().toISOString(),
      level,
      message,
      environment: process.env.NODE_ENV || "development",
      ...context,
    };
    
    // Output single-line JSON string for log aggregators
    const jsonOutput = JSON.stringify(logEntry);
    if (level === "ERROR") {
      console.error(jsonOutput);
    } else if (level === "WARN") {
      console.warn(jsonOutput);
    } else {
      console.log(jsonOutput);
    }
  }

  public static info(message: string, context?: LogContext): void {
    this.emit("INFO", message, context);
  }

  public static warn(message: string, context?: LogContext): void {
    this.emit("WARN", message, context);
  }

  public static error(message: string, error?: Error, context?: LogContext): void {
    this.emit("ERROR", message, {
      ...context,
      errorName: error?.name,
      errorMessage: error?.message,
      stack: error?.stack,
    });
  }
}
