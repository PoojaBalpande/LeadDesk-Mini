/**
 * Centralized Client & Server Environment Configuration.
 * Provides type-safe access to process.env variables with sensible fallback defaults.
 */

export const env = {
  /**
   * Application Brand / Title Name
   */
  appName: process.env.NEXT_PUBLIC_APP_NAME || "LeadDesk Mini",

  /**
   * Backend REST API Base URL
   */
  apiUrl: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",

  /**
   * Node Execution Environment ("development", "test", "production")
   */
  nodeEnv: process.env.NODE_ENV || "development",

  /**
   * Helper flag indicating if application is running in production mode
   */
  isProduction: process.env.NODE_ENV === "production",

  /**
   * Helper flag indicating if application is running in development mode
   */
  isDevelopment: process.env.NODE_ENV === "development",
} as const;

export type Env = typeof env;
