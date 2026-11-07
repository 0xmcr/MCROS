/**
 * @file secure-headers.ts
 * @description Production defensive security headers and CORS middleware for Node/Express/Next.js.
 * Mitigates XSS, Clickjacking, MIME sniffing, and cross-origin attacks.
 */

export interface SecurityHeadersConfig {
  isProduction: boolean;
  allowedOrigins: string[];
}

export function buildSecurityHeaders(config: SecurityHeadersConfig): Record<string, string> {
  const { isProduction, allowedOrigins } = config;

  // 1. Strict Content Security Policy (CSP)
  const cspDirectives = [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' https://fonts.gstatic.com",
    "img-src 'self' data: https:",
    "connect-src 'self' " + allowedOrigins.join(" "),
    "frame-ancestors 'none'", // Blocks Clickjacking
    "form-action 'self'",
    "base-uri 'self'",
    "upgrade-insecure-requests",
  ].join("; ");

  const headers: Record<string, string> = {
    // Defend against XSS via strict script execution bounds
    "Content-Security-Policy": cspDirectives,

    // Defend against Clickjacking (legacy browser fallback for frame-ancestors)
    "X-Frame-Options": "DENY",

    // Prevent MIME-type sniffing
    "X-Content-Type-Options": "nosniff",

    // Referrer control: protect private query parameters from leaking to third parties
    "Referrer-Policy": "strict-origin-when-cross-origin",

    // Disable unwanted browser sensors & hardware access
    "Permissions-Policy": "camera=(), microphone=(), geolocation=(), payment=()",
  };

  // Enforce HTTPS Strict Transport Security (HSTS) in production
  if (isProduction) {
    headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload";
  }

  return headers;
}
